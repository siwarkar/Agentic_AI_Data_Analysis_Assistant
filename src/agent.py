from langchain.chat_models import ChatOpenAI
from src.tools import basic_eda

def run_agent(df, question):
    llm = ChatOpenAI(temperature=0, model_name='gpt-3.5-turbo')
    eda = basic_eda(df)
    prompt = f'''
You are a data analysis assistant.
EDA Results: {eda}
User Question: {question}
Generate clear business insights.
'''
    return llm.predict(prompt)
