# Gitbot

Gitbot uses GitHub Actions to query an LLM (Large Language Model) and respond with useful insights or code snippets. The action is designed to run specific models from Ollama, with different commands based on the model specifications.

## How It Works
1. **Open an Issue**: To make a request, open a new issue in this repository.
2. **Model Name in Title**: Specify the model you want to use in the issue title (e.g., `Phi 3 Medium`).
3. **Query in the Body**: Type your query or question in the issue body.
4. **Wait for the Response**: GitHub Actions will run the specified model and reply to your issue. Be patient—depending on the model, this could take a few minutes.

> *Tip*: Since free AI resources can be slow, consider watching a quick video or taking a break while waiting!

## Available Models and Commands
| Model                  | Parameters | Size   | Command                       |
|------------------------|------------|--------|-------------------------------|
| Llama 3                | 8B         | 4.7GB  | `ollama run llama3`          |
| Llama 3                | 70B        | 40GB   | `ollama run llama3:70b`      |
| Phi 3 Mini             | 3.8B       | 2.3GB  | `ollama run phi3`            |
| Phi 3 Medium           | 14B        | 7.9GB  | `ollama run phi3:medium`     |
| Gemma                  | 2B         | 1.4GB  | `ollama run gemma:2b`        |
| Gemma                  | 7B         | 4.8GB  | `ollama run gemma:7b`        |
| Mistral                | 7B         | 4.1GB  | `ollama run mistral`         |
| Moondream 2            | 1.4B       | 829MB  | `ollama run moondream`       |
| Neural Chat            | 7B         | 4.1GB  | `ollama run neural-chat`     |
| Starling               | 7B         | 4.1GB  | `ollama run starling-lm`     |
| Code Llama             | 7B         | 3.8GB  | `ollama run codellama`       |
| Llama 2 Uncensored     | 7B         | 3.8GB  | `ollama run llama2-uncensored` |
| LLaVA                  | 7B         | 4.5GB  | `ollama run llava`           |
| Solar                  | 10.7B      | 6.1GB  | `ollama run solar`           |

## Benchmarks
Below is a table showing simple benchmarks for how long each model takes to complete a query. Note that performance may vary based on server load and the complexity of your request.

| Model                  | Completion Time | Notes                                        | Benchmarks                                    |              Pass/Fail
|------------------------|------------------|--------------------------------------------|------------------------------------------------------------------------------- |
| Phi 3 Mini             | 2m:37s          | Fast response, suitable for simpler queries | [Phi 3 Mini Benchmark](https://github.com/unaveragetech/Gitbot/issues/17)   | Pass
| Phi 3 Medium           | 5m:20s	         | Great for more complex code explanations    | [Phi3 medium Benchmark](https://github.com/unaveragetech/Gitbot/issues/18)  | pass
| Llama 3 (8B)           | 3m:20s	         | Good balance between speed and depth        | [Llama 3 8b Benchmark](https://github.com/unaveragetech/Gitbot/issues/19)   | pass
| Mistral                | 2m:41s	         | Very fast but less detailed                 | [Mistral Benchmark](https://github.com/unaveragetech/Gitbot/issues/20 )     | pass
| Moondream 2            | 1m:24s         | Quickest but limited in complexity        | [Unable to test without gpu](https://github.com/unaveragetech/Gitbot/issues/21)| Fail
| Neural Chat            | 3m:6s         | Effective for conversational queries        | [Neural Chat Benchmark](https://github.com/unaveragetech/Gitbot/issues/22)   | Pass
| Code Llama             | 3m:3s	         | Optimized for coding tasks                  |  [Code Llama Benchmark](https://github.com/unaveragetech/Gitbot/issues/23) | pass
| Llama 3 (70b)          | 1m:38s        | Large model by meta good for code generation |  [Too large for codespaces](https://github.com/unaveragetech/Gitbot/issues/25)| Fail
| Solar                  | pending         | Takes longer, but high detail               |   [Unfinished Benchmark](Undone_benchmark.md)|
| LLaVA                  | pending         | Ideal for visual language tasks             |   [Unfinished Benchmark](Undone_benchmark.md)|


### Example Benchmark
For a completed query example, see [this issue](https://github.com/unaveragetech/Gitbot/issues/17). It ran `Phi 3 Mini` and completed in **2 minutes and 37 seconds**, providing correct code with a detailed explanation. this same code will be repeated for all models over time and added to the Table i will also keep all tests and add thoes to the table as 
[Phi 3 Mini Benchmark](https://github.com/unaveragetech/Gitbot/issues/17)

this will also cache all models so its easier to run and takes less time on average 

## Additional Notes
- **Caching**: GitHub Actions uses caching to speed up subsequent runs by storing dependencies.
- **Customization**: You can extend the list of models or adjust the commands as needed.
- **Limitations**: Response time may be impacted by server availability, and more extensive models may require more processing time.

---
