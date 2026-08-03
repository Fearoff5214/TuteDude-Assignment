from dotenv import load_dotenv

load_dotenv()
from transformers import pipeline
from langchain_huggingface import HuggingFacePipeline
from langchain_core.prompts import ChatPromptTemplate, PromptTemplate
from langchain_core.output_parsers import StrOutputParser

#loading the model only one time so using this ew can call for other tasks also. Learned this from previous assignment
#which is reusable functions

pipe = pipeline("text2text-generation",model="google/flan-t5-base",max_new_tokens=100,)
llm = HuggingFacePipeline(pipeline=pipe)

#this is task 1 according to the assignment
# HuggingFace Model

print("=" * 60)
print("Simple HuggingFace Model Response")
print("=" * 60)
prompt = "Explain Artificial Intelligence in simple words."
response = llm.invoke(prompt)
print(response)

#lets do the task 2 from the assignment

prompt = PromptTemplate(input_variables=["topic"],template="Explain {topic} in simple terms.")
chain = prompt | llm | StrOutputParser()
topics = ["Machine Learning","Neural Networks","Cloud Computing"]
for topic in topics:
    print("\n---------------------------")
    print(f"Topic: {topic}")
    print(chain.invoke({"topic": topic}))

#task 3- chatprompt template in this task

chat_prompt = ChatPromptTemplate.from_messages([("system", "You are a helpful AI tutor."),("human", "Explain {topic} in easy language.")])
chain = chat_prompt | llm | StrOutputParser()
print("\n---------------------------")
print(chain.invoke({"topic": "Large Language Models"}))