
# pyrefly: ignore [missing-import]
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("Doc_loader/file.pdf")

doc = loader.load()

print(doc)