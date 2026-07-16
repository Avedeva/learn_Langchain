from langchain_community.document_loaders import TextLoader

loader = TextLoader("Doc_loader/The_Odyssey_Detailed_Study_Guide.txt", encoding="utf-8")

doc = loader.load()

print(doc)

print(doc[0])

