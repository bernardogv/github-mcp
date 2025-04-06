# github_mcp/server.py
import logging
import sys
import github_mcp.tools as tools
from mcp.server.fastmcp import FastMCP

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)
logger = logging.getLogger("github-mcp")

# Initialize FastMCP server
mcp = FastMCP("github")

# Register tools
mcp.tool()(tools.search_repositories)
mcp.tool()(tools.get_repo_issues)
mcp.tool()(tools.get_repo_info)

def main():
    """Run the MCP server."""
    try:
        logger.info("Starting GitHub MCP server...")
        logger.debug("Using transport: stdio")
        mcp.run(transport='stdio')
    except Exception as e:
        logger.error(f"Error running server: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()