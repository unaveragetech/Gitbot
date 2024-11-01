import os
import sys
import subprocess
from github import Github

# GitHub personal access token
GITHUB_TOKEN = os.getenv('GITHUB_TOKEN')
g = Github(GITHUB_TOKEN)

# Dictionary mapping model names to their Ollama run commands
model_commands = {
    "Llama 3": "ollama run llama3",
    "Llama 3 (70B)": "ollama run llama3:70b",
    "Phi 3 Mini": "ollama run phi3",
    "Phi 3 Medium": "ollama run phi3:medium",
    "Gemma (2B)": "ollama run gemma:2b",
    "Gemma (7B)": "ollama run gemma:7b",
    "Mistral": "ollama run mistral",
    "Moondream 2": "ollama run moondream",
    "Neural Chat": "ollama run neural-chat",
    "Starling": "ollama run starling-lm",
    "Code Llama": "ollama run codellama",
    "Llama 2 Uncensored": "ollama run llama2-uncensored",
    "LLaVA": "ollama run llava",
    "Solar": "ollama run solar",
}

def run_ollama_model(model_name, query):
    # Get the command for the specified model
    command = model_commands.get(model_name)

    if command is None:
        print(f"Model '{model_name}' not found. Please specify a valid model.")
        return None

    # Start the Ollama model and get the response
    process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Send the query to the model
    output, error = process.communicate(input=query)

    if process.returncode != 0:
        print(f"Error running model: {error}")
        return None
    
    return output

def write_response_to_file(model_name, query, response):
    filename = f"{model_name.replace(' ', '_')}_response.txt"
    with open(filename, 'w') as file:
        file.write(f"Model Name: {model_name}\n")
        file.write(f"Query: {query}\n")
        file.write(f"Response: {response}")

def respond_to_issue(issue, response):
    issue.create_comment(response)

def main(issue_number):
    # Get the issue from GitHub
    repo = g.get_repo("unaveragetech/Gitbot")  # replace with your username and repo name
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

