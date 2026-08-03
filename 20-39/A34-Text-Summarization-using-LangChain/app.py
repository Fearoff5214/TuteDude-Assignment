import os

from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate
from langchain_core.documents import Document
from langchain.chains.summarize import load_summarize_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter

load_dotenv()
llm = ChatGroq(model="llama-3.1-8b-instant",temperature=0)

# Task 1
with open("sample_article.txt", "r", encoding="utf-8") as file:
    text = file.read()

print("="*50)
print("Total Characters:", len(text))
print("="*50)
print(text[:500])
document = Document(page_content=text)

#task 2 - Prompt based summnarization

prompt = PromptTemplate(
    input_variables=["text"],
    template="""You are an expert summarizer.Summarize the following text{text}""")

#this prompt template willl be used to create the chain
chain = prompt | llm
summary = chain.invoke({"text": text})
print("\nPrompt Summary\n")
print(summary.content)

#Task 3 - Prompt Variations
short_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Summarize the text in only 5-6 lines{text}""")
#this is a short prompt compared to previous one/task
chain = short_prompt | llm
print("\nShort Summary\n")
print(chain.invoke({"text": text}).content)

#lets try the Bullet Summary
bullet_prompt = PromptTemplate(
    input_variables=["text"],
    template="""Summarize the following text using bullet points{text}""")
chain = bullet_prompt | llm
print("\nBullet Summary\n")
print(chain.invoke({"text": text}).content)

#now task5, this stuff chain
stuff_chain = load_summarize_chain(llm,chain_type="stuff")
stuff_summary = stuff_chain.invoke([document])
print("\nStuff Chain Summary\n")
print(stuff_summary["output_text"])

#Task 8 - Map Reduce
splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
docs = splitter.create_documents([text])
print("Chunks:", len(docs))
map_reduce_chain = load_summarize_chain(llm,chain_type="map_reduce")
map_summary = map_reduce_chain.invoke(docs)
print("\nMap Reduce Summary\n")
print(map_summary["output_text"])

#Task 11 - Refine Chain
refine_chain = load_summarize_chain(llm,chain_type="refine")
refine_summary = refine_chain.invoke(docs)
print("\nRefine Summary\n")
print(refine_summary["output_text"])

#now lets perform the reusable functions in this code
def summarize_document(text, method="map_reduce"):
    document = Document(page_content=text)
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000,chunk_overlap=100)
    docs = splitter.create_documents([text])
    if method == "prompt":
        prompt = PromptTemplate(
            input_variables=["text"],
            template="""Summarize the following text{text}""")

        chain = prompt | llm
        return chain.invoke({"text": text}).content
    elif method == "stuff":
        chain = load_summarize_chain(llm,chain_type="stuff")
        return chain.invoke([document])["output_text"]
    elif method == "map_reduce":
        chain = load_summarize_chain(llm,chain_type="map_reduce")
        return chain.invoke(docs)["output_text"]
    elif method == "refine":
        chain = load_summarize_chain(llm,chain_type="refine")
        return chain.invoke(docs)["output_text"]
    else:
        return "Invalid Method"
    
#examples can be like print(summarize_document(text, "stuff"))

print(summarize_document(text, "stuff"))
print(summarize_document(text, "map_reduce"))
print(summarize_document(text, "refine"))


#Task 9
print("\nChunk Summaries\n")
map_chain = load_summarize_chain(llm,chain_type="map_reduce",return_intermediate_steps=True)
result = map_chain.invoke(docs)
for i, summary in enumerate(result["intermediate_steps"], start=1):
    print(f"\nChunk {i}\n")
    print(summary)
print("\nFinal Summary\n")
print(result["output_text"])