import os
import subprocess
import json

# Example model command mapping (ensure these match your available models)
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
    # Normalize the model name to lower case
    normalized_model_name = model_name.lower()
    command = next((command for name, command in model_commands.items() if name.lower() == normalized_model_name), None)

    if command is None:
        print(f"Model '{model_name}' not found. Please specify a valid model.")
        return None

    # Split the command into a list for subprocess
    command_parts = command.split()  # This will split the command into parts
    command_parts.append(query)  # Append the query to the command

    # Start the Ollama model and get the response
    process = subprocess.Popen(command_parts, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    
    # Wait for the output and error
    output, error = process.communicate()

    if process.returncode != 0:
        print(f"Error running model: {error}")
        return None

    return output.strip()  # Return the output, stripped of leading/trailing whitespace

def main(issue_number):
    # Load issue data (mocking this for example purposes)
    model_name = "Llama 3"  # Replace with the actual model name from the issue
    query = "What color is the sky?"  # Replace with the actual query from the issue body

    print(f"Running Ollama interactor for issue number {issue_number}")
    response = run_ollama_model(model_name, query)

    if response:
        print(f"Response from model: {response}")

if __name__ == "__main__":
    issue_number = 4  # Example issue number
    main(issue_number)
