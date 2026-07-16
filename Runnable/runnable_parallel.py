from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence,RunnableParallel
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

api_key_1 = os.getenv("OPENROUTER_API_KEY")
api_key_2 = os.getenv("Laguna")

model_1 = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key_1,
    temperature=0,
    base_url="https://openrouter.ai/api/v1"

)


model_2 = ChatOpenAI(
   model = 'poolside/laguna-m.1:free',
    api_key=api_key_2,
    temperature=0,
    base_url="https://openrouter.ai/api/v1"
)

prompt_1 = PromptTemplate(
    template = "Generate a 5 line linkdin post on this topic :- {topic}",
    input_variables=['topic']

)



prompt_2 = PromptTemplate(
    template = "Generate a 5 line X post on this topic :- {topic}",
    input_variables=['topic']

)

parser = StrOutputParser()

parallel_chain = RunnableParallel(
    {'tweet':RunnableSequence(prompt_1,model_1,parser),
    'linkedin':RunnableSequence(prompt_2,model_2,parser)}
)

result = parallel_chain.invoke({"topic":"Artificial Intelligence"})

print(result['tweet'])
print('\n\n')
print(result['linkedin'])