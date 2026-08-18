Multi-Agent-System-using-LangGraph-MCP-Supervisor-Guardrails-HITL
A demo multi-agent system that uses LangGraph and MCP to implement a travel-planning assistant with a Supervisor, input Guardrails, and Human-In-The-Loop (HITL) approval flows. The project includes a FastAPI frontend, example MCP server, and client helpers to demonstrate how agents, supervisors, and guardrails can be composed into a safe, reviewable planning pipeline.

Key ideas:

Multi-agent coordination using LangGraph and MCP
Supervisor agent to manage complex workflows
Input guardrails to validate user requests
Human-in-the-loop approval for generated plans

Contents

app.py: FastAPI web frontend and API endpoints
backend.py: core agent orchestration / travel-planner logic
mcp_client.py: client helpers to interact with the MCP server
custom_weather_mcp_server.py: example MCP server for weather checks
templates/, static/: frontend UI assets (HTML, JS, CSS)
Features

Interactive web UI for sending travel planning prompts
Endpoint for drafting travel plans and separate approval endpoint
Example MCP server demonstrating domain adapters (weather, checkpoints)
Prerequisites

Python 3.10+ (recommended)
Git (to clone the repo)
A virtual environment tool (venv) or similar
Quick start (Windows)

Create and activate a virtual environment
python -m venv .venv
.venv\Scripts\Activate.ps1    # PowerShell
Install dependencies
pip install -r requirements.txt
Run the FastAPI app (development)
# option A (run module)
python app.py

# option B (uvicorn)
uvicorn app:app --reload --host 127.0.0.1 --port 8000
Open the web UI
Visit http://127.0.0.1:8000 in your browser to use the TripMate frontend.

Running the MCP server (example)

The repository includes custom_weather_mcp_server.py as an example MCP server. Run it in a separate terminal if you want to experiment with custom adapters used by the demo.
