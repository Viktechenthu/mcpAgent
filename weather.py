from mcp.server.fastmcp import FastMCP

mcp=FastMCP("Weather")

@mcp.tool()
async def get_weather(location: str) -> str:
    """ _summary_
    Get the current weather for a given location
    """
    # Placeholder implementation
    return f"The current weather in {location} is sunny with a temperature of 25°C."

if __name__ == "__main__":
    mcp.run(transport="streamable-http")