from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter
import faiss, os, pickle
import numpy as np

model = SentenceTransformer("all-MiniLM-L6-v2")
INDEX_PATH = "faiss.index"
META_PATH = "meta.pkl"

if os.path.exists(INDEX_PATH):
    index = faiss.read_index(INDEX_PATH)
    with open(META_PATH, "rb") as f:
        meta = pickle.load(f)
else:
    index = faiss.IndexFlatL2(384)
    meta = []

def create_or_update_faiss(filename, text):
    splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = splitter.split_text(text)
    embeds = model.encode(chunks)
    index.add(embeds)
    meta.extend(chunks)
    faiss.write_index(index, INDEX_PATH)
    with open(META_PATH, "wb") as f:
        pickle.dump(meta, f)

def embed_text(text):
    return model.encode([text])[0]

def search_faiss(query_vec, k=3):
    query_vec = np.array(query_vec).reshape(1, -1)
    D, I = index.search(query_vec, k)
    return [meta[i] for i in I[0] if i < len(meta)]