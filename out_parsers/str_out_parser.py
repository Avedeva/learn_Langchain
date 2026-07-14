from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
import os
from dotenv import load_dotenv


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


prompt_1 = template_1.invoke({"topic":'black hole'})

result_1 = model.invoke(prompt_1)

prompt_2 = template_2.invoke({"text":result_1.content})

result_2 = model.invoke(prompt_2)



print(result_1.content,"\n\n\n\n")
print("---------------------------------------------------------------------")
print(result_2.content)