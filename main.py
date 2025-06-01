from typing import List
from mcp.server.fastmcp import FastMCP

# Create an MCP server
mcp = FastMCP("Sound Effects")


# # Add an addition tool
# @mcp.tool()
# def add(a: int, b: int) -> int:
#     """Add two numbers"""
#     return a + b


# # Add a dynamic greeting resource
# @mcp.resource("greeting://{name}")
# def get_greeting(name: str) -> str:
#     """Get a personalized greeting"""
#     return f"Hello, {name}!"

@mcp.tool()
def find_sfx(folder_name: str) -> List[str]:
    "returns a list of all the available wooshes"
    
    
