from typing import List
from mcp.server.fastmcp import FastMCP
from get_audio_files import get_audio_files_recursive
from typing import Dict, List, Union
from move_audio_files import move_audio_files, parse_payload

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
    """Get audio files from a given folder
    
    Args: 
        folder_name: Enter the full path of folder for example - C:/Users/desce/OneDrive/Desktop/editing stock/sfx
    
    Returns: 
        list: List of relative paths to audio files (e.g., ['pack/audio1.wav', 'audio2.wav'])
    """
    
    response = get_audio_files_recursive(folder_name)

    return "\n---\n".join(response)

@mcp.tool()
def change_audio_location(json_payload: Union[str, List[Dict[str, str]]], root_folder: str) -> Dict[str, List[str]]:
    """
    Move audio files based on JSON payload within a specified root folder. Always pass the payload in python string format
    
    Args:
        json_payload: Either a JSON string or list of dictionaries with 'from' and 'to' keys
        root_folder: Root directory path where all operations will be performed
        
    Returns:
        Dictionary with 'success' and 'errors' lists containing operation results
        
    Example:
        payload = [{"from": "audio/song.wav", "to": "music/song.wav"}]
        result = move_audio_files(payload, "/home/user/project")
    """
    try:
        parsed_payload = parse_payload(json_payload)
        result = move_audio_files(parsed_payload, root_folder)
    except (ValueError, TypeError) as e:
        result = {"success": [], "errors": [str(e)]}


    return "\n---\n".join(result)