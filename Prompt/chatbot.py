from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage,AIMessage,HumanMessage
from langchain_core.prompts import load_prompt
import os

load_dotenv()

api_key = os.getenv("OPENROUTER_API_KEY")

model = ChatOpenAI(
   model = 'tencent/hy3:free',
    api_key=api_key,
    temperature=0.8,
    base_url="https://openrouter.ai/api/v1"

)


print("-------------------------------------------------\n")
print("---------------------------------  AI - Welcome How can i help you   -----------------------------------\n")
print("if u want to exit type exit in chat/console")

chat_history = [
    SystemMessage(content="You are a very good Therapist")
]


while True:
    user_promt = input("you :")
    chat_history.append(HumanMessage(content=user_promt))
    if user_promt == "exit":
        break

    result = model.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))
    print("------------------------------------------------------------\n")
    print("AI - ",result.content)
    print("------------------------------------------------------------\n")


print("\n\n",chat_history)










