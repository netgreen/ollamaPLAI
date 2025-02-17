from langchain.text_splitter import CharacterTextSplitter
from langchain.schema.document import Document
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaLLM
from langchain_ollama import OllamaEmbeddings
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate


global retriever
retriever = None

global rag_chain
rag_chain = None

def init():
	global retriever
	text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
	text = "I am going to tell you a story about Netanel. Netanel is 39 yaers old"
	docs = [Document(page_content=x) for x in text_splitter.split_text(text)]

	persist_directory = "/tmp/chromadb"
	vectorstore = Chroma.from_documents(documents=docs, collection_name="test",embedding=OllamaEmbeddings(model='nomic-embed-text'))
	retriever = vectorstore.as_retriever()
	
	
def init_conversation():
	global rag_chain
	llm = OllamaLLM(model="mistral", streaming=True)
	template = """Answer the question based only on the following context:{context} Question: {question}"""
	prompt = ChatPromptTemplate.from_template(template)
	rag_chain = ({"context": lambda x: retriever, "question": RunnablePassthrough()} | prompt | llm | StrOutputParser())
	
	
def chat(question):
	for chunk in rag_chain.stream(question):
    		if chunk:  # סינון None
            		yield chunk  
