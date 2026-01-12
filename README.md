# Agentic AI Data Analysis Assistant

An end-to-end **Agentic AI system** that performs **autonomous Exploratory Data Analysis (EDA)** and generates **business-ready insights** from uploaded datasets using **Large Language Models (LLMs)**.

This README covers **everything from project overview to local & cloud deployment**, written from a **production-grade data science perspective**.

---

## 1. Project Overview

Traditional EDA is time-consuming and repetitive. This project automates:

* Dataset understanding
* Statistical summarization
* Insight generation in natural language

The system behaves like a **data analyst agent**: it observes the data, reasons over statistics, and communicates insights clearly.

---

## 2. Key Features

* 📊 Automatic EDA (shape, columns, missing values, stats)
* 🤖 LLM-powered reasoning over EDA results
* 💬 Natural language business insights
* ⚡ API-first architecture
* 🖥️ Interactive Streamlit UI
* 🔌 Easily deployable

---

## 3. System Architecture

```
User
 │
 │ (CSV + Question)
 ▼
Streamlit UI
 │
 ▼
FastAPI Backend
 │
 ▼
Agent Layer (LangChain)
 │
 ▼
EDA Tools + LLM
 │
 ▼
Business Insights
```

---

## 4. Tech Stack

| Layer      | Technology             |
| ---------- | ---------------------- |
| UI         | Streamlit              |
| API        | FastAPI                |
| Agent      | LangChain              |
| LLM        | OpenAI GPT             |
| Data       | Pandas                 |
| Env Mgmt   | python-dotenv          |
| Deployment | Uvicorn / Docker-ready |

---

## 5. Project Structure

```
.
├── api/
│   └── main.py          # FastAPI backend (API entry point)
│
├── src/
│   ├── agent.py         # Agent logic (LLM + reasoning)
│   ├── tools.py         # EDA tools (statistics, profiling)
│   └── config.py        # Environment & API key loading
│
├── ui/
│   └── app.py           # Streamlit frontend
│
├── .env                 # Environment variables (OpenAI key)
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation
├── swap.ipynb           # Experimentation / prototyping notebook
└── .gitignore
```

.
├── app.py              # Streamlit frontend
├── main.py             # FastAPI entry point
├── agent.py            # Agent logic (LLM + EDA)
├── tools.py            # EDA utilities
├── config.py           # Environment configuration
├── requirements.txt    # Dependencies
├── .env                # API keys (not committed)
├── swap.ipynb          # Experimentation notebook
└── README.md

````

---

## 6. Environment Setup

### 6.1 Clone Repository
```bash
git clone <your-repo-url>
cd agentic-ai-eda
````

### 6.2 Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

### 6.3 Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 7. Environment Variables

Create a `.env` file in the root directory:

```
OPENAI_API_KEY=your_openai_api_key_here
```

> ⚠️ Never commit `.env` files to GitHub

---

## 8. How the Agent Works (Deep Dive)

### Step 1: Data Upload

* User uploads CSV via Streamlit

### Step 2: EDA Tool Execution

`basic_eda()` computes:

* Dataset shape
* Column names
* Missing values
* Descriptive statistics

### Step 3: Prompt Construction

EDA results + user question are injected into an LLM prompt.

### Step 4: LLM Reasoning

The model converts raw statistics into **business insights**.

---

## 9. Running the Application Locally

### 9.1 Start FastAPI Backend

```bash
uvicorn main:app --reload
```

API runs at:

```
http://127.0.0.1:8000
```

### 9.2 Start Streamlit Frontend

```bash
streamlit run app.py
```

UI runs at:

```
http://localhost:8501
```

---

## 10. API Documentation

### Endpoint

`POST /analyze`

### Inputs

* CSV File
* Question (query parameter)

### Response

```json
{
  "insight": "Generated business insight here"
}
```

---

## 11. Example Use Cases

* Sales performance analysis
* Customer churn exploration
* Marketing funnel diagnostics
* Operations & supply chain analysis

---

## 12. Deployment Options

### Option 1: Local VM / Server

* Use `uvicorn` + `nginx`

### Option 2: Docker (Recommended)

**Dockerfile (example):**

```dockerfile
FROM python:3.10
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

### Option 3: Cloud Platforms

* AWS EC2
* Azure App Service
* Google Cloud Run
* Railway / Render

---

## 13. Security Best Practices

* Never expose API keys
* Add file size limits
* Validate CSV schema
* Add rate limiting for production

---

## 14. Future Improvements

* Multi-agent collaboration
* Chart generation (auto-visuals)
* Memory-based agents
* Vector database integration
* Role-based insights (CEO, Analyst, Marketing)

---

## 15. Bullet

> Built an **Agentic AI Data Analysis Assistant** using **LLMs + LangChain** that automates EDA and generates business insights, reducing manual analysis effort by ~50%.

---

## 16. Author

**Developed by:
## Swapnil Iwarkar
** Data Scientist / ML Engineer

