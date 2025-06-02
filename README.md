
# 🎧 SFX Server – MCP Audio Asset Manager

An **MCP (Model Context Protocol)**-compatible server that enables intelligent access and organization of audio files through AI agents or automation systems. Built using `FastMCP`, it supports discovering sound effects and relocating audio assets across a structured folder hierarchy.

---

## 🔧 Features

* **Discover Sound Effects**
  List all audio files recursively from any specified folder.

* **Move Audio Files**
  Move or reorganize audio files using a simple JSON payload.

* **MCP-Compliant Interface**
  Exposes tools usable by AI agents and automation engines via the Model Context Protocol.

---

## 🗂️ Project Structure

```bash
SFX_SERVER/
│
├── main.py                # MCP server initialization and tool registration
├── get_audio_files.py     # Recursively collects audio file paths
├── move_audio_files.py    # Handles moving files and payload parsing
│
├── pyproject.toml         # Project metadata and dependency configuration
├── uv.lock                # Dependency lock file
├── .gitignore
├── .python-version
├── README.md              # You're reading it
```

---

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/bhaveshsinghal95182/sfx_server
cd sfx_server
```

### 2. Install Dependencies (via [`uv`](https://github.com/astral-sh/uv))

```bash
uv pip install .
```

### 3. Register the MCP Server

```bash
uv run mcp install main.py
```

This command installs and registers the MCP server named **"Sound Effects"**, exposing its tools for interaction.

---

## 🛠️ Tools

### `find_sfx(folder_name: str) → List[str]`

Recursively fetches all audio file paths from a specified folder.

**Arguments**:

* `folder_name`: Full path to the folder (e.g., `C:/Users/you/Desktop/audio`)

**Returns**:

* List of relative audio file paths.

---

### `change_audio_location(json_payload: str | List[Dict[str, str]], root_folder: str) → Dict[str, List[str]]`

Moves audio files from one location to another within the defined root directory.

**Arguments**:

* `json_payload`: A JSON string or list of `{ "from": "...", "to": "..." }` entries
* `root_folder`: Absolute path where all operations are confined

**Returns**:

* `{ "success": [...], "errors": [...] }`

---

## 🧠 Use Cases

* 🛠️ Automating post-production workflows
* 🧬 Contextual file management with LLM agents
* 🎬 Structuring large audio libraries for editors
* 🤖 Agentic systems that require audio file discovery and relocation

---

## 🔐 Security Note

This tool performs direct file operations on your filesystem. Always scope the `root_folder` securely and validate access in AI contexts to avoid unintended behavior.


---

## 📫 Feedback & Contributions

Issues, ideas, and pull requests are welcome.

---
