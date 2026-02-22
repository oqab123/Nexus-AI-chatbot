# 🧠 NEXUS AI — Ultimate Personal AI Assistant

> **Python + Groq LLM + RAG + Voice + Web Search + SQLite Memory**

---

## ⚡ Features

| Feature | Technology | Description |
|---------|-----------|-------------|
| 🤖 **LLM Chat** | Groq + LLaMA 3 | Ultra-fast AI conversation |
| 📄 **PDF/RAG** | pdfplumber + chunking | Chat with your documents |
| 🌐 **Web Search** | DuckDuckGo API | Real-time internet search |
| 🎤 **Voice Input** | Groq Whisper v3 | Speech-to-text transcription |
| 🧠 **Auto Memory** | SQLite3 | Remembers facts about you |
| 📚 **Chat History** | SQLite3 | Persistent session storage |

---

## 🚀 Quick Start

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Run
streamlit run app.py

# 3. Open browser → http://localhost:8501
# 4. Enter Groq API key in sidebar
```

## 🔑 Get Free Groq API Key

1. Go to **console.groq.com**
2. Sign up (free)
3. API Keys → Create New Key
4. Copy → paste in app sidebar

---

## 🎮 How to Use Each Mode

### 💬 Chat Mode
Normal conversation with your AI. Supports multiple personas:
- NEXUS (default), Developer, Data Analyst, Writer, Professor

### 📄 PDF/RAG Mode
1. Upload any PDF file
2. AI reads and chunks the document
3. Ask questions → AI finds relevant sections and answers

### 🌐 Web Search Mode
- Type any query
- AI searches DuckDuckGo in real-time
- Responds with current information + source links

### 🎤 Voice Mode
1. Upload WAV/MP3/M4A audio file
2. Groq Whisper transcribes it
3. Click "Send to Chat" → AI responds

### 🧠 Memory Mode
- AI automatically extracts and saves facts from conversations
- Manually add facts (name, preferences, etc.)
- All memories used as context in future chats

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────┐
│              NEXUS AI System                 │
├─────────────┬───────────────────────────────┤
│  Frontend   │  Streamlit (Python Web UI)     │
├─────────────┼───────────────────────────────┤
│  LLM Engine │  Groq API → LLaMA 3 / Mixtral │
├─────────────┼───────────────────────────────┤
│  RAG System │  PDF → Chunks → Retrieval      │
├─────────────┼───────────────────────────────┤
│  Web Search │  DuckDuckGo API               │
├─────────────┼───────────────────────────────┤
│  Voice      │  Groq Whisper Large v3        │
├─────────────┼───────────────────────────────┤
│  Memory     │  SQLite3 (auto-persistent)    │
└─────────────┴───────────────────────────────┘
```

---

## 📁 Project Structure

```
ultimate-ai-assistant/
├── app.py              # Complete application (1 file!)
├── requirements.txt    # Python dependencies
├── README.md           # This file
└── nexus_memory.db     # Auto-created SQLite database
```

---

## 🛠️ Models Available

| Model | Speed | Quality | Best For |
|-------|-------|---------|----------|
| llama-3.3-70b-versatile | ⚡⚡⚡ | ⭐⭐⭐⭐⭐ | Best overall |
| llama-3.1-8b-instant | ⚡⚡⚡⚡⚡ | ⭐⭐⭐ | Ultra fast |
| mixtral-8x7b-32768 | ⚡⚡⚡ | ⭐⭐⭐⭐ | Long documents |
| gemma2-9b-it | ⚡⚡⚡ | ⭐⭐⭐⭐ | Google's model |

---

Made with ❤️ | Python + Groq + Streamlit
