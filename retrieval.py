from langchain_community.document_loaders import DirectoryLoader, PyMuPDFLoader

# フォルダ配下のすべてのPDFを読み込む
loader = DirectoryLoader(
    "/content/data",         # フォルダのパス    
    glob="**/*.pdf",              # 再帰的にすべてのPDFを対象
    loader_cls=PyMuPDFLoader      # 個々のPDFを読み込むクラス
)

documents = loader.load()
len(documents)

len(documents[0].page_content)

from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
   chunk_size=500,
    chunk_overlap=30,
    separator="\n",
)

splitted_pages = text_splitter.split_documents(documents)
len(splitted_pages)

len(splitted_pages[0].page_content)

from langchain.embeddings.openai import OpenAIEmbeddings
embeddings = OpenAIEmbeddings(model="text-embedding-3-small")

from langchain.vectorstores import Chroma
import os

chroma_db = "/content/.healthX_db"

if os.path.exists(chroma_db):
    # すでにDBが存在する場合 ⇒ 読み込み
    db = Chroma(
        persist_directory=chroma_db,
        embedding_function=embeddings
    )
else:
    # DBが存在しない場合 ⇒ 新規作成
    db = Chroma.from_documents(
        splitted_pages,
        embedding=embeddings,
        persist_directory=chroma_db
    )
  
db.persist()

retriever = db.as_retriever()

from langchain.chains import RetrievalQA
from langchain.chat_models import ChatOpenAI

llm = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.5)

chain = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=retriever)

query = "HealthXの無料プランについて教えてください。"

result = chain.run(query)

print(result)