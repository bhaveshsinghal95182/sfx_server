import json
import os
import shutil
from pathlib import Path
from typing import List, Dict, Union

def move_audio_files(json_payload: Union[str, List[Dict[str, str]]], root_folder: str) -> Dict[str, List[str]]:
    """
    Move audio files based on JSON payload within a specified root folder.
    
    Args:
        json_payload: Either a JSON string or list of dictionaries with 'from' and 'to' keys
        root_folder: Root directory path where all operations will be performed
        
    Returns:
        Dictionary with 'success' and 'errors' lists containing operation results
        
    Example:
        payload = [{"from": "audio/song.wav", "to": "music/song.wav"}]
        result = move_audio_files(payload, "/home/user/project")
    """
    
    # Parse JSON payload if it's a string
    if isinstance(json_payload, str):
        try:
            file_operations = json.loads(json_payload)
        except json.JSONDecodeError as e:
            return {"success": [], "errors": [f"Invalid JSON: {str(e)}"]}
    else:
        file_operations = json_payload
    
    # Validate root folder exists
    root_path = Path(root_folder)
    if not root_path.exists():
        return {"success": [], "errors": [f"Root folder does not exist: {root_folder}"]}
    
    if not root_path.is_dir():
        return {"success": [], "errors": [f"Root path is not a directory: {root_folder}"]}
    
    success_operations = []
    error_operations = []
    
    for operation in file_operations:
        try:
            # Validate operation structure
            if not isinstance(operation, dict) or 'from' not in operation or 'to' not in operation:
                error_operations.append(f"Invalid operation format: {operation}")
                continue
            
            from_path = operation['from']
            to_path = operation['to']
            
            # Construct full paths within root folder
            source_file = root_path / from_path
            destination_file = root_path / to_path
            
            # Security check: ensure paths are within root folder
            try:
                source_file.resolve().relative_to(root_path.resolve())
                destination_file.resolve().relative_to(root_path.resolve())
            except ValueError:
                error_operations.append(f"Path outside root folder detected: {from_path} or {to_path}")
                continue
            
            # Check if source file exists
            if not source_file.exists():
                error_operations.append(f"Source file not found: {source_file}")
                continue
            
            # Check if source is actually a file
            if not source_file.is_file():
                error_operations.append(f"Source is not a file: {source_file}")
                continue
            
            # Create destination directory if it doesn't exist
            destination_file.parent.mkdir(parents=True, exist_ok=True)
            
            # Check if destination already exists
            if destination_file.exists():
                error_operations.append(f"Destination already exists: {destination_file}")
                continue
            
            # Move the file
            shutil.move(str(source_file), str(destination_file))
            success_operations.append(f"Moved: {from_path} -> {to_path}")
            
        except Exception as e:
            error_operations.append(f"Error processing {operation}: {str(e)}")
    
    return {
        "success": success_operations,
        "errors": error_operations
    }

def parse_payload(json_input: Union[str, List[Dict[str, str]]]) -> List[Dict[str, str]]:
    if isinstance(json_input, str):
        try:
            parsed = json.loads(json_input)
            if not isinstance(parsed, list):
                raise ValueError("Parsed JSON is not a list of operations.")
            return parsed
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON string: {str(e)}")
    elif isinstance(json_input, list):
        return json_input
    else:
        raise TypeError("json_input must be a list or JSON string.")


def main():
    """Main function for command line usage"""
    import argparse
    
    parser = argparse.ArgumentParser(description='Move audio files based on JSON configuration')
    parser.add_argument('--root-folder', 
                       default="C:/Users/desce/OneDrive/Desktop/editing stock/sfx",
                       help='Root folder path for file operations')
    parser.add_argument('--json-file', help='Path to JSON file containing move operations')
    parser.add_argument('--json-string', help='JSON string containing move operations')
    parser.add_argument('--woosh', action='store_true', 
                       help='Move woosh files to woosh/ subdirectory')
    
    args = parser.parse_args()
    
    # Handle woosh-specific operation
    if args.woosh:
        payload = [
            {"from": "woosh-230554.mp3", "to": "woosh/woosh-230554.mp3"},
            {"from": "woosh-260275.mp3", "to": "woosh/woosh-260275.mp3"}
        ]
    # Load JSON payload from file or string
    elif args.json_file:
        with open(args.json_file, 'r') as f:
            payload = f.read()
    elif args.json_string:
        payload = args.json_string
    else:
        print("Please provide either --woosh, --json-file, or --json-string")
        return
    
    # Execute file moves
    result = move_audio_files(payload, args.root_folder)

    print(result)
    
    # Print results
    print("=== SUCCESSFUL OPERATIONS ===")
    for success in result["success"]:
        print(f"✓ {success}")
    
    print("\n=== ERRORS ===")
    for error in result["errors"]:
        print(f"✗ {error}")
    
    print(f"\nSummary: {len(result['success'])} successful, {len(result['errors'])} errors")

if __name__ == "__main__":
    main()