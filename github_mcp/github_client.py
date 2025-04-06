# github_mcp/github_client.py
import os
from typing import Optional
from github import Github
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_github_client(access_token: Optional[str] = None) -> Github:
    """Get a GitHub client using provided token or from environment."""
    token = access_token or os.environ.get("GITHUB_TOKEN")
    if not token:
        raise ValueError("GitHub token must be provided or set as GITHUB_TOKEN environment variable")
    return Github(token)