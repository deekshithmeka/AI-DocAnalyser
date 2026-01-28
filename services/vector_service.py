import chromadb
from sentence_transformers import SentenceTransformer

# Load embedding model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Create Chroma client
client = chromadb.Client()

# Collection
collection = client.create_collection(name="documents")


def add_documents(text):
    global collection

    # Recreate collection to clear old data
    try:
        client.delete_collection(name="documents")
    except:
        pass

    collection = client.create_collection(name="documents")

    chunks = split_text(text)

    embeddings = model.encode(chunks).tolist()
    ids = [str(i) for i in range(len(chunks))]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids
    )


def query_documents(question, top_k=3):
    q_embedding = model.encode([question]).tolist()

    results = collection.query(
        query_embeddings=q_embedding,
        n_results=top_k
    )

    return results["documents"][0]


def split_text(text, chunk_size=500):
    words = text.split()
    chunks = []
    current = []

    for word in words:
        current.append(word)
        if len(current) >= chunk_size:
            chunks.append(" ".join(current))
            current = []

    if current:
        chunks.append(" ".join(current))

    return chunks
