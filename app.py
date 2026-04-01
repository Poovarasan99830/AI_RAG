import chromadb
import shutil
import os

DB_PATH = "db"

# Try to close existing connections safely.
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
