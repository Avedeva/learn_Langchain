from langchain_community.document_loaders import WebBaseLoader

url = "https://www.amazon.in/Replacement-Compatible-Chromebook-Elitebook-Pavilion/dp/B0F6VHMRVL/ref=sr_1_8?sr=8-8"
loader = WebBaseLoader(url)

doc = loader.load()

print(len(doc))