# main.py
import sys
import logging
from github_mcp.github_client import get_github_client
from github_mcp.tools import search_repositories, get_repo_issues, get_repo_info
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("github-mcp")

# Initialize FastMCP server
mcp = FastMCP("github")

# Register tools
mcp.tool()(search_repositories)
mcp.tool()(get_repo_issues)
mcp.tool()(get_repo_info)

def main():
    """Run the MCP server."""
    try:
        logger.info("Starting GitHub MCP server...")
        mcp.run(transport='stdio')
    except Exception as e:
        logger.error(f"Error running server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()