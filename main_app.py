import streamlit as st
from file_utils import extract_text_from_file , extract_text_from_url
from vector_utils import create_or_update_faiss, embed_text, search_faiss
from mistral_llm import get_mistral_response
from sarvam_llm import get_sarvam_response
from db_utils import store_chat, fetch_chat_history, clear_chat_history
from redis_utils import is_rate_limited, get_cached_response, cache_response, clear_cache, cache_stats
from dotenv import load_dotenv
import os
load_dotenv()


st.title("📚 AI Document Chatbot (Mistral + Sarvam)")

uploaded_file = st.file_uploader("Upload a file", type=["pdf", "txt", "docx", "csv", "json", "html", "xml"])
url = st.text_input("Or enter a URL to fetch content:")
if uploaded_file:
    text = extract_text_from_file(uploaded_file)
    create_or_update_faiss(uploaded_file.name, text)
    st.success("Text extracted and indexed with FAISS")

if url:
    try:
        text = extract_text_from_url(url)
        create_or_update_faiss(url, text)
        st.success("Text extracted from URL and indexed with FAISS")
    except Exception as e:
        st.error(f"Failed to fetch URL: {e}")

query = st.text_input("Ask a question:")
user_id = "user"  # or session_id
if query:
    if is_rate_limited(user_id):
        st.error("Rate limit exceeded. Try again later.")
    else:
        cached = get_cached_response(query)
        if cached:
            response = cached
        else:
            vec = embed_text(query)
            context = "\n".join(search_faiss(vec, k=3))
            prompt = f"Use the following context to answer:\n{context}\n\nQuestion: {query}"
            response = get_mistral_response(prompt)
            if "error" in response.lower():
                response = get_sarvam_response(prompt)
            cache_response(query, response)

        st.markdown("**AI Response:** " + response)
        store_chat("user", query)
        store_chat("ai", response)

if st.checkbox("Show chat history"):
    for _, role, msg in fetch_chat_history():
        st.markdown(f"**{role.capitalize()}:** {msg}")

if st.button("🗑️ Clear Chat History"):
    clear_chat_history()
    st.success("Chat history cleared")

if st.button("🧹 Clear Redis Cache"):
    clear_cache()
    st.success("Redis cache cleared")

hits, misses = cache_stats()
st.markdown(f"**Cache Hits:** {hits} | **Cache Misses:** {misses}")