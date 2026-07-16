from langchain_community.document_loaders import PyPDFLoader,DirectoryLoader

loader = DirectoryLoader(
    path = "Doc_loader/Books",
    glob = "*.pdf",
    loader_cls=PyPDFLoader
)

docs = loader.load()

print(len(docs))