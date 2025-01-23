# rag_manager.py
import chromadb
from langchain.text_splitter import RecursiveCharacterTextSplitter

class NarrativeRAG:
    def __init__(self):
        self.client = chromadb.PersistentClient(path="./chroma_db")
        self.collection = self.client.get_or_create_collection("narrative")
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=500,
            chunk_overlap=50
        )

    def index_context(self, document: dict, metadata: dict):
        chunks = self.text_splitter.split_text(document)
        ids = [str(uuid.uuid4()) for _ in chunks]
        self.collection.add(
            documents=chunks,
            metadatas=[metadata]*len(chunks),
            ids=ids
        )

    def retrieve_context(self, query, k=3):
        results = self.collection.query(
            query_texts=[query],
            n_results=k
        )
        return [doc for doc in results['documents'][0]]