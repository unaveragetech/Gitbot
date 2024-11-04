#ollama_interacter.py
import os
import subprocess
import json
import requests
import sys

# Example model command mapping
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

def load_config():
    """Load the configuration from config.json."""
    try:
        with open("config.json", "r") as file:
            config = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        raise Exception("Failed to load config.json. Make sure the file exists and is valid JSON.")
    
    # Validate that essential fields are present
    if "repo_owner" not in config or "repo_name" not in config:
        raise Exception("config.json must include 'repo_owner' and 'repo_name'.")
    
    return config

def get_issue_data(issue_number):
    """Fetch issue data from GitHub."""
    config = load_config()  # Load configuration
    repo_owner = config["repo_owner"]
    repo_name = config["repo_name"]

    # Define the issue URL
    issue_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}"
    
    # Prepare headers with the GitHub token for authentication
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }
    
    # Fetch issue data
    response = requests.get(issue_url, headers=headers)
    if response.status_code == 200:
        issue_data = response.json()
        model_name = issue_data['title']  # Assuming model name is in the issue title
        query = issue_data['body']        # Query is the body of the issue
        return model_name, query
    else:
        print(f"Failed to fetch issue data: {response.content}")
        return None, None

def run_ollama_model(model_name, query):
    """Run the Ollama model with the given model name and query."""
    normalized_model_name = model_name.lower()
    command = next((cmd for name, cmd in model_commands.items() if name.lower() == normalized_model_name), None)
    
    if command is None:
        print(f"Model '{model_name}' not found. Please specify a valid model.")
        return None

    command_parts = command.split()  # Split the command into parts
    command_parts.append(query)      # Append the query to the command

    # Start the Ollama model and get the response
    process = subprocess.Popen(command_parts, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    output, error = process.communicate()

    if process.returncode != 0:
        print(f"Error running model: {error}")
        return None

    # Write the output to response.txt
    with open("response.txt", "w") as response_file:
        response_file.write(output.strip())
    
    print("Response written to response.txt.")
    return output.strip()

def write_response_to_github_issue(issue_number, response):
    """Write the model's response as a comment on the GitHub issue."""
    config = load_config()
    repo_owner = config["repo_owner"]
    repo_name = config["repo_name"]

    # Define the comment URL
    comment_url = f"https://api.github.com/repos/{repo_owner}/{repo_name}/issues/{issue_number}/comments"
    
    # Prepare headers with the GitHub token for authentication
    headers = {
        "Authorization": f"token {os.getenv('GITHUB_TOKEN')}",
        "Accept": "application/vnd.github.v3+json",
    }
    
    # Prepare the payload
    data = {"body": response}
    
    # Send the comment to GitHub
    response = requests.post(comment_url, headers=headers, json=data)
    if response.status_code == 201:
        print("Successfully commented on the issue.")
    else:
        print(f"Failed to comment on the issue: {response.content}")

def main(issue_number):
    """Main function to run the Ollama interactor."""
    print(f"Running Ollama interactor for issue number {issue_number}")
    model_name, query = get_issue_data(issue_number)
    
    if model_name and query:
        response = run_ollama_model(model_name, query)
        if response:
            print(f"Response from model: {response}")
            write_response_to_github_issue(issue_number, response)
        else:
            print("No response received from the model.")
    else:
        print("Could not retrieve model name and query from the issue.")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python ollama_interactor.py <issue_number>")
        sys.exit(1)

    issue_number = sys.argv[1]
    main(issue_number)
