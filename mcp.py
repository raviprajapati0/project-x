import os
from pathlib import Path
from typing import Any

import requests
from dotenv import load_dotenv
from mcp.server.fastmcp import FastMCP


BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env")

mcp = FastMCP("Weather MCP Server")

OPENWEATHER_API_KEY = os.getenv(
    "OPENWEATHER_API_KEY"
)

REQUEST_TIMEOUT_SECONDS = 20

