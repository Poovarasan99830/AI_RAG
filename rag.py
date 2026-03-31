import os
import shutil
import chromadb
from flask import Flask, request, jsonify
import requests
import json

# --------------------------------------
# 🔥 AUTO DELETE OLD ChromaDB
# --------------------------------------
DB_PATH = "db"

# Try to close existing connections safely
try:
    client = chromadb.PersistentClient(path=DB_PATH)
    client.reset()
    print("🔥 Chroma reset successfully.")
except Exception as e:
    print("⚠ No active Chroma client to reset.", e)

# Safe folder delete
if os.path.exists(DB_PATH):
    try:
        shutil.rmtree(DB_PATH)
        print("🔥 Old DB folder deleted.")
    except PermissionError:
        print("❌ Windows locked the DB folder.")

print("✔ Ready to create new DB.")





# --------------------------------------
# OLLAMA SETTINGS
# --------------------------------------
OLLAMA_URL = "http://localhost:11434/api"
EMBED_MODEL = "nomic-embed-text"
CHAT_MODEL = "llama3"






# --------------------------------------
# OLLAMA FUNCTIONS
# --------------------------------------
def ollama_embed(text):
    """Generate embeddings from Ollama using a real embedding model."""
    resp = requests.post(
        f"{OLLAMA_URL}/embed",
        json={"model": EMBED_MODEL, "input": text}
    )

    if resp.status_code != 200:
        raise Exception("Embedding model error: " + resp.text)

    data = resp.json()
    return data["embeddings"][0]


def ollama_chat(prompt):
    """Chat with Llama3 using streaming output."""
    resp = requests.post(
        f"{OLLAMA_URL}/chat",
        json={
            "model": CHAT_MODEL,
            "messages": [{"role": "user", "content": prompt}],
            "stream": True
        },
        stream=True
    )

    final_answer = ""
    for line in resp.iter_lines():
        if line:
            data = json.loads(line.decode("utf-8"))
            if "message" in data:
                final_answer += data["message"]["content"]

    return final_answer


DB_PATH = "db"

# Create persistent client
client = chromadb.PersistentClient(path=DB_PATH)



def get_collection():
    try:
        return client.get_collection("rag_docs")
    except:
        return client.create_collection(
            name="rag_docs",
            metadata={"hnsw:space": "cosine"}
        )


print("✅ Fresh rag_docs collection created")

# --------------------------------------
# INGEST FUNCTION
# --------------------------------------





def ingest_text(path):
    collection = get_collection()   # 🔥 always fresh

    with open(path, "r", encoding="utf-8") as f:
        text = f.read()

    CHUNK_SIZE = 1000
    chunks = [text[i:i+CHUNK_SIZE] for i in range(0, len(text), CHUNK_SIZE)]

    for i, chunk in enumerate(chunks):
        chunk = chunk.strip()
        if not chunk:
            continue

        emb = ollama_embed(chunk)

        collection.add(
            ids=[f"chunk_{i}"],
            documents=[chunk],
            embeddings=[emb]
        )

    return "Ingestion completed successfully"



# --------------------------------------
# RAG ANSWERING
# --------------------------------------




def rag_answer(query, n_results=10):
    collection = get_collection()   # 🔥 always fresh

    q_emb = ollama_embed(query)

    results = collection.query(
        query_embeddings=[q_emb],
        n_results=n_results
    )

    docs = results["documents"][0] if results["documents"] else []
    if not docs:
        return "No matching data found."

    ctx = "\n\n".join(docs[:5])
    return ollama_chat(f"Context:\n{ctx}\n\nQuestion: {query}")


# --------------------------------------
# FLASK API
# --------------------------------------
app = Flask(__name__)

@app.route("/")
def home():
    return "RAG API is running ✔ (Ollama + ChromaDB + Flask)"

@app.route("/ingest", methods=["POST"])
def ingest_api():
    path = request.json.get("path")
    msg = ingest_text(path)
    return jsonify({"message": msg})

@app.route("/ask", methods=["POST"])
def ask_api():
    q = request.json.get("question")
    ans = rag_answer(q)
    return jsonify({"answer": ans})


if __name__ == "__main__":
    app.run(debug=True, use_reloader=False)
