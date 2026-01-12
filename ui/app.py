import streamlit as st, requests

API='http://127.0.0.1:8000/analyze'

st.title('📊 Agentic AI Data Analysis Assistant')

file = st.file_uploader('Upload CSV', type='csv')
question = st.text_input('What insight do you want?')

if st.button('Analyze') and file:
    files = {'file': file}
    params = {'question': question}
    r = requests.post(API, files=files, params=params)
    st.write(r.json()['insight'])
