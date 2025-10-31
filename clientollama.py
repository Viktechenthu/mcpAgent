from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain.chat_models import Ollama

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            
            "weather": {
                "transport": "streamable_http",
                "url": "http://localhost:8000/mcp"  # Adjust the URL if needed
            }
        }
    )

    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()

    model = Ollama(model="llama3.1", base_url="http://localhost:11434")
    agent = create_agent(model, tools)

    # math_response = await agent.ainvoke(
    #     {
    #         "message": [{"role": "user", "content": "What is (3 + 5) * 2?"}],
    #     }
    # )
    # print("Math Response:", math_response['message'][-1]['content'])

    weather_response = await agent.ainvoke(
        {
            "messages": [{"role": "user", "content": "How is weather in New York today?"}],
        }
    )
    print("Weather Response:", weather_response['messages'][-1].content)
    
if __name__ == "__main__":
    asyncio.run(main())