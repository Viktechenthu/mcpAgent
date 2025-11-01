# MCP Agent — Local client runner

Small project demonstrating a LangChain agent that uses MCP tools and a local model.

Prerequisites
- Python 3.11+ installed
- Git (repo already cloned)
- If you use Ollama: ollama installed and at least one model pulled
- A working MCP tool process (e.g. mathserver or an HTTP MCP endpoint) if your tools configuration requires it

Quick steps — recommended (from project root)
1. Open a terminal and (optional) stop conda base auto-activation for the session:
   ```
   conda deactivate
   ```

2. Create or activate the project virtualenv (.venv)
   ```
   cd /Users/sareev/Documents/Learning/mcpAgent

   # If .venv doesn't exist (create fresh venv with pip)
   python3 -m venv .venv --upgrade-deps

   # Activate the venv
   source .venv/bin/activate
   ```

3. Ensure pip is available (if needed)
   ```
   python -m ensurepip --default-pip
   python -m pip install --upgrade pip setuptools wheel
   ```

4. Install dependencies
   - Option A: install directly
     ```
     python -m pip install langchain langchain-mcp-adapters langchain-groq groq langgraph python-dotenv
     ```
   - Option B: (if you prefer a requirements file) create `requirements.txt` and run:
     ```
     python -m pip install -r requirements.txt
     ```

5. Configure environment variables
   - Create a `.env` file (this repo ignores `.env`) and add keys as needed:
     ```
     # Example for Groq
     GROQ_API_KEY=your_groq_api_key_here
     ```
   - If you plan to use Ollama instead of Groq, start the Ollama daemon:
     ```
     # ensure ollama is installed, then:
     ollama pull <model-name>
     ollama serve
     ```

6. Ensure any MCP tool servers or subprocess tools your config relies on are running (e.g. mathserver, or the HTTP endpoint at `http://localhost:8000/mcp`).

Run the client
- Using the Groq-backed client (client.py):
  ```
  source .venv/bin/activate
  python client.py
  ```

- Using the Ollama-backed client (clientollama.py):
  ```
  source .venv/bin/activate
  python clientollama.py
  ```

Troubleshooting
- If `ModuleNotFoundError: No module named 'langchain'` appears, make sure you activated the same venv where you installed packages (check `which python`).
- If `python -m pip` is missing in the venv, run `python -m ensurepip --default-pip` or recreate the venv with `python3 -m venv .venv --upgrade-deps`.
- If you see JSON/streaming errors from stdio MCP tools, run subprocess tools unbuffered (e.g. use `python -u ...`) and make servers resilient to blank lines.
- For branch protection, git config, or commit user management, see GitHub docs (not repeated here).

License / Notes
- This README is a minimal run guide. Adjust model names, endpoints and environment variables to your setup.