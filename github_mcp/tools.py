# github_mcp/tools.py
from typing import List, Optional
from github_mcp.github_client import get_github_client

async def search_repositories(query: str, limit: int = 5) -> str:
    """Search for GitHub repositories.
    
    Args:
        query: Search query for repositories
        limit: Maximum number of results to return (default: 5)
    """
    try:
        g = get_github_client()
        repositories = g.search_repositories(query=query, sort="stars")
        
        results = []
        for i, repo in enumerate(repositories[:limit]):
            results.append(f"""
Repository: {repo.full_name}
Description: {repo.description or 'No description'}
Stars: {repo.stargazers_count}
Language: {repo.language or 'Not specified'}
URL: {repo.html_url}
""")
            
        if not results:
            return "No repositories found matching your query."
            
        return "\n---\n".join(results)
    except Exception as e:
        return f"Error searching repositories: {str(e)}"

async def get_repo_issues(repo_name: str, state: str = "open", limit: int = 5) -> str:
    """Get issues from a GitHub repository.
    
    Args:
        repo_name: Repository name in format 'owner/repo'
        state: Issue state ('open', 'closed', 'all')
        limit: Maximum number of issues to return (default: 5)
    """
    try:
        g = get_github_client()
        repo = g.get_repo(repo_name)
        
        issues = repo.get_issues(state=state)
        
        results = []
        for i, issue in enumerate(issues[:limit]):
            results.append(f"""
Issue #{issue.number}: {issue.title}
State: {issue.state}
Created: {issue.created_at}
URL: {issue.html_url}
""")
            
        if not results:
            return f"No {state} issues found in {repo_name}."
            
        return "\n---\n".join(results)
    except Exception as e:
        return f"Error retrieving issues: {str(e)}"

async def get_repo_info(repo_name: str) -> str:
    """Get detailed information about a GitHub repository.
    
    Args:
        repo_name: Repository name in format 'owner/repo'
    """
    try:
        g = get_github_client()
        repo = g.get_repo(repo_name)
        
        return f"""
Repository: {repo.full_name}
Description: {repo.description or 'No description'}
Owner: {repo.owner.login}
Stars: {repo.stargazers_count}
Forks: {repo.forks_count}
Open Issues: {repo.open_issues_count}
Default Branch: {repo.default_branch}
Created: {repo.created_at}
Last Updated: {repo.updated_at}
Language: {repo.language or 'Not specified'}
License: {repo.license.name if repo.license else 'No license'}
URL: {repo.html_url}
"""
    except Exception as e:
        return f"Error retrieving repository information: {str(e)}"