from langchain_ollama import ChatOllama
from dotenv import load_dotenv

if __name__ == "__main__":

    load_dotenv()
    
    #llm = ChatOllama(model="gemma3:4b")
    llm = ChatOllama(model="llama3.2")
    messages = [
        ("system", "사용자가 입력한 문장을 영어로 번역해."),
        ("human", "내일은 피자를 먹어야지!")
    ]

    result = llm.invoke(messages)
    print(result)