from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnableSequence,RunnableBranch,RunnablePassthrough
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser,PydanticOutputParser
from pydantic import BaseModel,Field
from typing import Literal
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




class Sentiment(BaseModel):

    sentiment:Literal['positive','Negative'] = Field(
        description='The sentiment of email either Positive or Negative'
    )

py_parser = PydanticOutputParser(pydantic_object=Sentiment)

prompt_classify = PromptTemplate(
    template='Classify this {email} based on the sentiment positive or negaitive {format_instructions}',
    input_variables=['emial'],
    partial_variables={
        'format_instructions':py_parser.get_format_instructions()
    }
)
prompt_positive = PromptTemplate(
    template='Based on the {emotion} mail generate reply email.',
    input_variables=['emotion'],
)

prompt_negative = PromptTemplate(
    template='Based on the ${emotion} mail generate reply email.',
    input_variables=['emotion'],
)


parser = StrOutputParser()

prompt_gen = PromptTemplate(
    template = 'Make a emial haiving {emotion} emotion',
    input_variables=['emotion']
)
email_gen_chain = RunnableSequence(prompt_gen,model,parser,prompt_classify,model,py_parser)




decision_chain = RunnableBranch(
    (lambda x : x.sentiment == 'positive',RunnableSequence(prompt_positive,model,parser)),
    (lambda x : x.sentiment == 'Negative',RunnableSequence(prompt_negative,model,parser)),
    RunnablePassthrough()


)


chain = email_gen_chain|decision_chain

result = chain.invoke({'emotion':'Happy'})

print(result)