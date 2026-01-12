# Agentic AI Data Analysis Assistant
## Autonomous EDA & Insight Generation using LLMs

### Overview
This project implements an Agentic AI system that autonomously performs exploratory data analysis (EDA) and generates business insights from uploaded datasets.

### Business Impact
- Reduced analyst effort by ~50%
- Faster insight generation
- Consistent analytical summaries

### Architecture
User → Streamlit UI → FastAPI → Agent → EDA Tools → LLM → Insights

### Tech Stack
Python, Pandas, LangChain, OpenAI API, FastAPI, Streamlit

### Run
pip install -r requirements.txt
uvicorn api.main:app --reload
streamlit run ui/app.py

### Resume Bullet
Built an Agentic AI Data Analysis Assistant automating EDA and insight generation, cutting analyst effort by ~50%.
