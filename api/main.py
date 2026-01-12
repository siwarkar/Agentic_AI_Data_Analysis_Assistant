from fastapi import FastAPI, UploadFile
import pandas as pd
from src.agent import run_agent

app = FastAPI(title='Agentic AI Data Analysis Assistant')

@app.post('/analyze')
async def analyze(file: UploadFile, question: str):
    df = pd.read_csv(file.file)
    answer = run_agent(df, question)
    return {'insight': answer}
