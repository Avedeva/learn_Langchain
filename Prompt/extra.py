from langchain_core.prompts import ChatPromptTemplate,MessagesPlaceholder,load_prompt
from langchain_core.messages import HumanMessage,AIMessage

template = ChatPromptTemplate([
('system','you ara a genz girl with lot of boys wanting to talk to u in a mood of {mood}'),
( 'human','hey chitra {expression}')

])

prompt = template.invoke({'mood':'bitchy','expression':'flirty'})

print(prompt)


# MESSAGE PLACE HOLDER ()


#chat template

chat_temp = ChatPromptTemplate([

    ('system','You are a helpful  customer support agent'),
    MessagesPlaceholder(variable_name='chat_history'),
    ('human','{query}')
])

# LOAD CHAT HISTORY
chat_history = []
with open('Prompt/CHAT_HISTORY.txt') as f:
    for line in f.readlines():
        line = line.strip()

        if line.startswith('Human') :
            chat_history.append(HumanMessage(content=line))

        elif line.startswith("AI"):
            chat_history.append(HumanMessage(content=line))



print(chat_history)


# assign value

prompt = chat_temp.invoke({'chat_history':chat_history,'query':'refund time ?'})


prompt.save('CHAT_HISTORY.txt')