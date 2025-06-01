import os
from pathlib import Path

def get_audio_files_recursive(root_path):
    """
    Recursively finds all audio files in a given directory and returns their paths
    relative to the root directory.
    
    Args:
        root_path (str): Path to the root directory to search in
        
    Returns:
        list: List of relative paths to audio files (e.g., ['pack/audio1.wav', 'audio2.wav'])
    """
    # Common audio file extensions
    audio_extensions = {
        '.wav', '.mp3', '.flac', '.aac', '.ogg', '.wma', '.m4a', 
        '.aiff', '.au', '.ra', '.3gp', '.amr', '.ac3', '.dts'
    }
    
    audio_files = []
    root_path = Path(root_path)
    
    # Check if the root path exists
    if not root_path.exists():
        raise FileNotFoundError(f"The path '{root_path}' does not exist")
    
    if not root_path.is_dir():
        raise NotADirectoryError(f"The path '{root_path}' is not a directory")
    
    # Walk through all files and subdirectories
    for file_path in root_path.rglob('*'):
        if file_path.is_file():
            # Check if the file has an audio extension (case-insensitive)
            if file_path.suffix.lower() in audio_extensions:
                # Get relative path from root
                relative_path = file_path.relative_to(root_path)
                # Convert to forward slashes for consistency (works on Windows too)
                relative_path_str = str(relative_path).replace('\\', '/')
                audio_files.append(relative_path_str)
    
    return sorted(audio_files)  # Return sorted list for consistent ordering

# Example usage:
if __name__ == "__main__":
    # Example usage
    try:
        root_folder = "C:/Users/desce/OneDrive/Desktop/editing stock/sfx"  # Replace with your actual path
        audio_files = get_audio_files_recursive(root_folder)
        
        print(f"Found {len(audio_files)} audio files:")
        for audio_file in audio_files:
            print(f"  {audio_file}")
            
    except (FileNotFoundError, NotADirectoryError) as e:
        print(f"Error: {e}")