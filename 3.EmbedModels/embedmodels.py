from langchain_huggingface import HuggingFaceEmbeddings


embeddings = HuggingFaceEmbeddings(model_name = 'sentence-transformers/all-MiniLM-L6-v2')

documents = [
    "niggas in paris"
]

vector  = embeddings.embed_documents(documents)

print(str(vector))