from dotenv import load_dotenv
load_dotenv()

from langchain.agents import create_agent


def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

agent = create_agent(
    model="gpt-4o",
    tools=[get_weather],
    system_prompt="You are a helpful assistant",
)

def main():
    print("Hello from langchain-course!")

    # Run the agent
    # LLM이 자연어를 보고 tool 호출을 “결정하면서” 인자를 스스로 생성한다
    result= agent.invoke(
        {"messages": [{"role": "user", "content": "what is the weather in sf?"}]}
    )

    print(result["messages"][-1].content)

if __name__ == "__main__":
    main()
