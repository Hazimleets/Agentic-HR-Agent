from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
import os

# Load the documents
loader = TextLoader("docs.txt")  # or your desired file
documents = loader.load()

# Split into chunks
text_splitter = CharacterTextSplitter(chunk_size=50, chunk_overlap=10)
texts = text_splitter.split_documents(documents)

# Create embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Create FAISS vector store
db = FAISS.from_documents(texts, embedding)
db.save_local("hr_faiss_index")
print("[SUCCESS] Vector store saved to hr_faiss_index/")
