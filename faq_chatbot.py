from langchain.chains import create_history_aware_retriever, create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_community.vectorstores import FAISS
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_groq import ChatGroq
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.document_loaders import TextLoader
from dotenv import load_dotenv
import os

# Load .env once when module is loaded
load_dotenv()
api_key = os.getenv("GROQ_API_KEY")
if not api_key:
    raise EnvironmentError("GROQ_API_KEY not found in environment variables.")

# Load FAQ file and initialize chain at module level
faq_path = os.path.join(os.path.dirname(__file__), "faq.txt")
if not os.path.exists(faq_path):
    raise FileNotFoundError("faq.txt file is missing.")

loader = TextLoader(faq_path, encoding="utf-8")
documents = loader.load()

llm = ChatGroq(groq_api_key=api_key, model="gemma2-9b-it")
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
splits = text_splitter.split_documents(documents)
vectorstore = FAISS.from_documents(splits, embeddings)
retriever = vectorstore.as_retriever()

# Prompt templates
contextualize_q_prompt = ChatPromptTemplate.from_messages([
    ("system", "Given a chat history and the latest user question which may reference context, reformulate it to be self-contained."),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])
history_aware_retriever = create_history_aware_retriever(llm, retriever, contextualize_q_prompt)

qa_prompt = ChatPromptTemplate.from_messages([
    ("system", "You are an assistant that answers questions based on the FAQ context. "
              "If the question is not answerable, respond with 'I don't know'. "
              "If unrelated, say 'This question is not related to the FAQ.'\n\nContext:\n{context}"),
    MessagesPlaceholder("chat_history"),
    ("human", "{input}")
])
qa_chain = create_stuff_documents_chain(llm, qa_prompt)
rag_chain = create_retrieval_chain(history_aware_retriever, qa_chain)

# Shared session store
session_store = {}

def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in session_store:
        session_store[session_id] = ChatMessageHistory()
    return session_store[session_id]

# Build the conversation-aware chain
conversational_rag_chain = RunnableWithMessageHistory(
    rag_chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="chat_history",
    output_messages_key="answer"
)

# 🟢 This is the main function you'll call from Flask or backend
def run_faq_bot(user_input: str, session_id: str = "default_user") -> str:
    try:
        response = conversational_rag_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        return response["answer"]
    except Exception as e:
        return f"An error occurred: {str(e)}"
