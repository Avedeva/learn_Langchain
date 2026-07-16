from langchain_core.runnables import RunnableSequence,RunnableParallel,RunnablePassthrough,RunnableLambda
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=0.8,
    base_url="https://openrouter.ai/api/v1"

)

prompt1 = PromptTemplate(
    template="Tell mejoke about {topic}",
    input_variables=['topic'])

prompt2 = PromptTemplate(
    template = "explan me this {text}",
    input_variables=['text']
)

parser = StrOutputParser()

def count(text):
    return len(text.split())



joke_gen_chain = RunnableSequence(prompt1,model,parser)


parallel_chain = RunnableParallel({
    'joke':RunnablePassthrough(),
    'word_count':RunnableLambda(count)
})

chain = joke_gen_chain|parallel_chain
result = chain.invoke({'topic':'mom like yo mama so fat she exhales and cyclone comes'})
print(result)