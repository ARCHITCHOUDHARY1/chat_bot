# 📚 AI Document Chatbot (Mistral + Sarvam)

An advanced AI-powered chatbot that allows users to upload documents or provide URLs, extracts and indexes content, and answers questions using powerful LLMs like Mistral and Sarvam. It leverages semantic search (FAISS), PostgreSQL for chat history, and Redis for caching—all within a user-friendly Streamlit interface.

---

## 🚀 Features

- **📁 File Upload:** Accepts PDF, DOCX, TXT, CSV, JSON, HTML, XML.
- **🔗 URL Input:** Extracts and indexes webpage content.
- **🧠 Semantic Search:** Uses FAISS + Sentence Transformers for contextual retrieval.
- **🤖 LLM Integration:** Responds using Mistral and Sarvam APIs.
- **🗃️ Chat History:** Stores session data in PostgreSQL.
- **⚡ Fast & Safe:** Redis-based caching and rate limiting.
- **🖼️ Modern Interface:** Built with Streamlit for smooth interaction.

---

## 🗂️ Project Structure

```
chat_bot/
├── main_app.py            # Streamlit UI and logic
├── file_utils.py          # File/URL text extraction logic
├── vector_utils.py        # Embeddings + FAISS search logic
├── mistral_llm.py         # Mistral API integration
├── sarvam_llm.py          # Sarvam API integration
├── db_utils.py            # PostgreSQL chat history operations
├── redis_utils.py         # Redis for caching and rate limiting
├── requirements.txt       # Required Python packages
├── docker-compose.yml     # For PostgreSQL + Redis containers
├── .env                   # API keys & configuration
└── README.md              # Documentation
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/ARCHITCHOUDHARY1/chat_bot.git
cd chat_bot
```

### 2. Create a `.env` File

```ini
# .env
MISTRAL_API_KEY=your_mistral_api_key
SARVAM_API_KEY=your_sarvam_api_key

POSTGRES_DB=chatbotdb
POSTGRES_USER=chatbotuser
POSTGRES_PASSWORD=strongpassword
POSTGRES_HOST=localhost
POSTGRES_PORT=5432

REDIS_HOST=localhost
REDIS_PORT=6379
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start PostgreSQL and Redis (Docker)

```bash
docker-compose up -d
```

### 5. Launch the App

```bash
streamlit run main_app.py
```

---

## 🖥️ How to Use

1. Upload a document or paste a URL.
2. Ask questions based on uploaded/linked content.
3. View chatbot responses and session history.
4. Use optional controls to clear chat or Redis cache.

---

## 🛠️ Troubleshooting

| Issue | Solution |
|-------|----------|
| **Database/Redis errors** | Ensure Docker is running, and `.env` matches `docker-compose.yml`. |
| **Missing modules** | Verify all Python files exist and dependencies are installed. |
| **API key errors** | Confirm your Mistral and Sarvam API keys are valid. |

---

## 📸 Screenshots
![Screenshot (24)](https://github.com/user-attachments/assets/b8056864-4c12-4303-8eb8-83402b26eeee)
![Screenshot (25)](https://github.com/user-attachments/assets/766ceb5d-1aea-4160-b22b-b13ee09a81c6)


> *(Include UI screenshots here for better visual reference.)*

---

## 👤 Author

- **Name:** Archit Choudhary  
- **Date:** June 2025  

---

## 📄 License

This project is provided **for educational and demonstration purposes only**.  
Feel free to modify and extend it under the terms of the [MIT License](LICENSE).
