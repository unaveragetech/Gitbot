import os
import sys
import subprocess
from github import Github

# GitHub personal access token
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
g = Github(GITHUB_TOKEN)

def run_ollama_model(model_name, query):
    # Start the Ollama model and get the response
    command = f"ollama run {model_name}"
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Send the query to the model
    output, error = process.communicate(input=query)

    if process.returncode != 0:
        print(f"Error running model: {error}")
        return None
    
    return output

def write_response_to_file(model_name, query, response):
    filename = f"{model_name}_response.txt"
    with open(filename, 'w') as file:
        file.write(f"Model Name: {model_name}\n")
        file.write(f"Query: {query}\n")
        file.write(f"Response: {response}")

def respond_to_issue(issue, response):
    issue.create_comment(response)

def main(issue_number):
    # Get the issue from GitHub
    repo = g.get_repo("your_username/your_repo_name")  # replace with your username and repo name
    issue = repo.get_issue(issue_number)

    # Parse model name and query from the issue title and body
    model_name = issue.title.strip()  # Get model name from the title
    query = issue.body.strip()         # Get query from the body

    # Run the Ollama model
    response = run_ollama_model(model_name, query)

    if response:
        write_response_to_file(model_name, query, response)
        respond_to_issue(issue, response)
    else:
        print("Failed to get a response from the model.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ollama_interactor.py <issue_number>")
        sys.exit(1)

    issue_number = int(sys.argv[1])
    main(issue_number)
