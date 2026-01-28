# 📄 DocAnlzeR – AI-Powered Document Intelligence Platform

DocAnlzeR is an AI-powered web application that allows users to upload one or multiple PDF documents, automatically generate structured study notes, and chat with their documents using intelligent, context-aware AI responses.

It uses:
- Groq’s LLaMA models for AI
- Chroma Vector Database for smart retrieval (RAG)
- Flask for the backend
- Bootstrap for the UI

This project is designed for students, researchers, and professionals to quickly understand and interact with large documents.

---

## 🚀 Features

- 📂 Upload **multiple PDFs at once**
- 🧠 **Auto Notes Generator**
  - Summary
  - Key Points
  - Important Terms
- 💬 **Chat with Documents**
  - Ask questions from uploaded PDFs
  - Context-based answers using RAG
- 🎯 Answer Modes:
  - Simple
  - Exam-Oriented
  - Technical
- 📊 Chat History
- 📤 Export Notes as PDF
- 🧩 Modular, industry-style architecture

---

## 🛠 Tech Stack

- Frontend: HTML, CSS, Bootstrap  
- Backend: Python, Flask  
- AI: Groq API (Meta LLaMA models)  
- Vector DB: Chroma  
- Embeddings: Sentence-Transformers  
- PDF Processing: pdfplumber  
- PDF Export: ReportLab  

---

🧠 How It Works

1. User uploads one or more PDFs
2. Text is extracted from all documents
3. Documents are split into chunks
4. Chunks are converted into embeddings
5. Stored in Chroma Vector Database
6. On each question:
7. Relevant chunks are retrieved
8. Sent to LLaMA (Groq)
9. Context-aware answer is generated
