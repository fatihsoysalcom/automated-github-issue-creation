import os
import openai
from github import Github

# --- Configuration ---
# Ensure you have your OpenAI API key and GitHub token set as environment variables
# export OPENAI_API_KEY='your-openai-api-key'
# export GITHUB_TOKEN='your-github-personal-access-token'

# Replace with your GitHub repository (e.g., 'owner/repo')
GITHUB_REPO_NAME = os.environ.get("GITHUB_REPO_NAME", "your-username/your-repo")

# --- LLM Prompting ---
# This prompt guides the LLM to extract relevant information for GitHub issues.
# It's designed to be specific and structured for better results.
ISSUE_PROMPT_TEMPLATE = """
Analyze the following text, which is a summary of a bug report or user feedback.
Extract the following information and format it as a JSON object:

1.  `title`: A concise, descriptive title for the GitHub issue (max 70 characters).
2.  `body`: A detailed description of the issue, including steps to reproduce if applicable, expected behavior, and actual behavior. Use Markdown formatting.
3.  `labels`: A list of relevant labels (e.g., 'bug', 'enhancement', 'documentation', 'question').

If the text does not contain enough information to create a meaningful issue, return an empty JSON object `{}`.

Text to analyze:
"""
{text}
"""

JSON output:
"""
