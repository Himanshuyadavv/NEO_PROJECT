# 🚀 NeoStats AI Chatbot

An AI-powered document analysis chatbot that enables users to upload TXT documents and extract insights through natural language conversations. Built using **Streamlit**, **Google Gemini AI**, and **RAG (Retrieval-Augmented Generation)**.

---

## ✨ Features

- 📄 Upload and analyze TXT documents
- 🤖 AI-powered question answering
- 📝 Concise and Detailed response modes
- 🌙 Light/Dark theme support
- 💬 Chat history management
- ⚠️ Robust error handling
- ☁️ Streamlit Cloud deployment ready

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| Frontend | Streamlit |
| Backend | Python |
| AI Model | Google Gemini 1.5 Flash |
| Vector Database | FAISS |
| Retrieval | RAG |
| Deployment | Streamlit Cloud |

---

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
Document Processing
 │
 ▼
Text Chunking
 │
 ▼
FAISS Vector Store
 │
 ▼
Gemini AI
 │
 ▼
Response Generation
 │
 ▼
User Response
```

---

## 🔄 Workflow

1. Upload a TXT document.
2. Extract and preprocess text.
3. Generate embeddings and store in FAISS.
4. Ask questions related to the document.
5. Retrieve relevant context using RAG.
6. Generate responses using Gemini AI.
7. Display answers in Concise or Detailed mode.

---

## 📂 Project Structure

```text
NeoStats-AI-Chatbot/
│
├── app.py
├── requirements.txt
├── .env
├── README.md
│
├── data/
│
├── utils/
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── vector_store.py
│   └── response_generator.py
│
└── assets/
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/your-username/neostats-ai-chatbot.git
cd neostats-ai-chatbot
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Run Locally

```bash
streamlit run app.py
```

Application will run at:

```text
http://localhost:8501
```

---

## ☁️ Deployment

Deploy directly on **Streamlit Cloud**:

1. Push project to GitHub.
2. Connect repository to Streamlit Cloud.
3. Add Gemini API key in Secrets.
4. Deploy.

---

## 📈 Future Enhancements

- PDF & DOCX support
- Multi-language support
- Advanced RAG retrieval
- User authentication
- Document management
- Mobile application
- Analytics dashboard

---
