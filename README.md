## AI Fact Checker Web App

An AI-powered fact-checking web application that verifies claims extracted from documents or text using **Large Language Models (LLMs)** and **real-time web search**. The system combines OpenAI’s reasoning capabilities with Tavily’s search API to provide evidence-backed claim verification.

---

## Assignment Notes
- Built as part of an AI Fact-Checking assignment
- Uses OpenAI for reasoning and Tavily for live search
- Focused on modular, readable, and extensible design


---

## 🎥 Demo Video: https://drive.google.com/file/d/1fYLIedx9vucz9O2t36aAEjQQY-z-j0vr/view?usp=drive_link

## Features

* 📄 **PDF/Text Input Support** – Upload PDFs or enter raw text
* 🧠 **Automatic Claim Extraction** – Identifies factual claims using NLP
* 🔍 **Real-Time Web Search** – Fetches reliable sources via Tavily API
* ✅ **AI-Based Verification** – Classifies claims as *True / False / Uncertain*
* 🧾 **Source-backed Explanations** – Provides reasoning with citations
* 🌐 **Streamlit UI** – Simple and interactive web interface

---

## 🏗️ Project Structure

```
ai-fact-checker/
│
├── app.py                  # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md               # Project documentation
├── .gitignore              # Ignored files (API keys, cache, venv)
│
└── utils/
    ├── __init__.py
    ├── pdf_reader.py       # PDF text extraction logic
    ├── claim_extractor.py  # Claim extraction using NLP / LLM
    └── fact_verifier.py    # Fact verification using OpenAI + Tavily
```

---

## ⚙️ Tech Stack

* **Frontend**: Streamlit
* **Backend / Logic**: Python
* **LLM**: OpenAI API
* **Search Engine**: Tavily API
* **Environment Management**: python-dotenv

---

## 🔑 API Keys Setup (Required)

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
TAVILY_API_KEY=your_tavily_api_key_here
```

## 🧪 How It Works (Pipeline)

1. **Input**: User uploads a PDF or enters text
2. **Extraction**: Claims are extracted from the content
3. **Search**: Tavily fetches relevant web evidence
4. **Verification**: OpenAI evaluates claims against sources
5. **Output**: Claims labeled with explanations and sources

---

## 📊 Output Example

* **Claim**: *“The Great Wall of China is visible from space.”*
* **Verdict**: ❌ False
* **Explanation**: Astronaut reports and NASA sources confirm it is not visible to the naked eye.
* **Sources**: NASA, National Geographic

---

## 🔐 Security & Privacy

* API keys stored securely using environment variables
* `.env` file excluded from version control
* No user data stored permanently

---

## 🚧 Limitations

* Results depend on web data availability
* API rate limits apply (OpenAI & Tavily)
* Extremely vague claims may return *Uncertain*

---

## 👩‍💻 Author

**Kashvi Ruhela**
GitHub: [https://github.com/kashvi666](https://github.com/kashvi666)



