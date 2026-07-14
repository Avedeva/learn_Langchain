from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
import os
import streamlit as st

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
    model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=0.8,
    base_url="https://openrouter.ai/api/v1"

)




st.header("Research Tool")

paper_text = st.selectbox('Select Paper Name',["Attention is All you need","Bert"])

analysis_type = st.selectbox('Select Explanation Type' ,["Beginner Friendly","moderate","Hard 🍆"])

length = st.selectbox('Selct the length of output',["5 lines","10 lines","15 lines"])

template=load_prompt('template.json')

prompt = template.invoke({
    "paper_text":paper_text,
    "analysis_type":analysis_type,
    "length":length
})

if st.button("Summarize"):
    result = model.invoke(prompt)
    st.write(result.content)


