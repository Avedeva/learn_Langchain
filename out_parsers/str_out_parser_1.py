from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser


load_dotenv()
api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=0.8,
    base_url="https://openrouter.ai/api/v1"

)


# review  template

template_1 = PromptTemplate(
    template= "write a detailed report on {topic}",
    input_variables=['topic']
)

# summary template


template_2 = PromptTemplate(
    template= "write a summary of 5 line to this {text}",
    input_variables=['text']
)

parser = StrOutputParser()


chain = template_1 | model | parser | template_2 | model | parser


result = chain.invoke({'topic' : 'black hole'})


print(result)