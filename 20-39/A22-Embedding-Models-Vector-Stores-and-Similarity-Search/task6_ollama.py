from langchain_community.embeddings import OllamaEmbeddings

embedding_model = OllamaEmbeddings(model="nomic-embed-text")
embedding = embedding_model.embed_query("Artificial Intelligence is transforming healthcare.")

print("Embedding Length:", len(embedding))
print(embedding[:10])