from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.chains import RetrievalQA

from transformers import pipeline
from langchain_community.llms import HuggingFacePipeline

# Load local sentence-transformer for embeddings
embedding = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

# Load the FAISS vector store
vectordb = FAISS.load_local("hr_faiss_index", embedding, allow_dangerous_deserialization=True)

# Load a local text-to-text generation pipeline (FLAN-T5)
hf_pipeline = pipeline(
    "text2text-generation",
    model="google/flan-t5-base",          # You can change to flan-t5-small if needed
    tokenizer="google/flan-t5-base",
    max_length=512
)

# Use the local pipeline with LangChain
llm = HuggingFacePipeline(pipeline=hf_pipeline)

# Load QA chain
retriever = vectordb.as_retriever()
qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)

# Function to handle answer generation
def generate_answer(question):
    result = qa_chain.run(question)
    return result
