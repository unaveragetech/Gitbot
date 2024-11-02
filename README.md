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

---
[suggest a new addition](https://github.com/unaveragetech/Gitbot/issues/33)
---

## Benchmarks

Below is a table showing simple benchmarks for how long each model takes to complete a query. Note that performance may vary based on server load and the complexity of your request.

| Model                  | Completion Time | Notes                                        | Benchmarks                                      | Pass/Fail |
|------------------------|------------------|----------------------------------------------|------------------------------------------------|-----------|
| Phi 3 Mini             | 2m:37s           | Fast response, suitable for simpler queries  | [Phi 3 Mini Benchmark](https://github.com/unaveragetech/Gitbot/issues/17) | Pass      |
| Phi 3 Medium           | 5m:20s           | Great for more complex code explanations     | [Phi 3 Medium Benchmark](https://github.com/unaveragetech/Gitbot/issues/18) | Pass      |
| Llama 3 (8B)          | 3m:20s           | Good balance between speed and depth         | [Llama 3 8B Benchmark](https://github.com/unaveragetech/Gitbot/issues/19) | Pass      |
| Mistral                | 2m:41s           | Very fast but less detailed                  | [Mistral Benchmark](https://github.com/unaveragetech/Gitbot/issues/20) | Pass      |
| Moondream 2            | 1m:24s           | Quickest but limited in complexity           | [Unable to test without GPU](https://github.com/unaveragetech/Gitbot/issues/21) | Fail      |
| Neural Chat            | 3m:06s           | Effective for conversational queries         | [Neural Chat Benchmark](https://github.com/unaveragetech/Gitbot/issues/22) | Pass      |
| Code Llama             | 3m:03s           | Optimized for coding tasks                   | [Code Llama Benchmark](https://github.com/unaveragetech/Gitbot/issues/23) | Pass      |
| Llama 3 (70B)         | 1m:38s           | Large model by Meta, good for code generation | [Too large for Codespaces](https://github.com/unaveragetech/Gitbot/issues/25) | Fail      |
| Solar                  | 4m               | Takes longer, but high detail                | [Solar Benchmark](https://github.com/unaveragetech/Gitbot/issues/26)   | Pass      |
| LLaVA                  | 2m:31s           | Ideal for visual language tasks              | [LLaVA Benchmark](https://github.com/unaveragetech/Gitbot/issues/27)   | Pass      |
| Llama 2 Uncensored     | 2m:48s           | Uncensored Llama 2 model                     | [Llama 2 Uncensored Benchmark](https://github.com/unaveragetech/Gitbot/issues/28) | Pass      |
| Gemma (2B)            | 1m:32s           | High-performing and efficient                 | [Gemma (2B) Benchmark](https://github.com/unaveragetech/Gitbot/issues/29) | Pass      |
| Gemma (7B)            | 3m                | High-performing and efficient                 | [Gemma (7B) Benchmark](https://github.com/unaveragetech/Gitbot/issues/30) | Pass      |
| Starling               | 2m:50s           | Large language model trained by reinforcement learning | [Starling Benchmark](https://github.com/unaveragetech/Gitbot/issues/31) | Pass      |

### Example Benchmark
For a completed query example, see [this issue](https://github.com/unaveragetech/Gitbot/issues/17). It ran `Phi 3 Mini` and completed in **2 minutes and 37 seconds**, providing correct code with a detailed explanation. The same code will be repeated for all models over time, and results will be added to the table.

## Model Use Cases

### Recommended Models for Different Use Cases
---

## Model Use Cases

### Recommended Models for Different Use Cases
all times in this section are related to the benchmark from [Benchmark information on how the test is configured this test will not be changed and will be used to test all llm's that are added to the system](Undone_benchmark.md)

1. **Simple Queries**:
   - **Phi 3 Mini**: Fastest response at **2m:37s**, suitable for straightforward requests. (Pass)
   - **Moondream 2**: Quickest completion time of **1m:24s**, but limited in complexity. (Fail Unable to run)

2. **Complex Code Explanations**:
   - **Phi 3 Medium**: Excellent for detailed explanations, taking **5m:20s**. (Pass)
   - **Llama 3 (8B)**: Balances speed and depth effectively with a response time of **3m:20s**. (Pass)

3. **Conversational Tasks**:
   - **Neural Chat**: Effective for generating conversational responses, completing queries in **3m:06s**. (Pass)

4. **Coding Tasks**:
   - **Code Llama**: Optimized for programming-related queries, taking **3m:03s**. (Pass)
   - **Gemma (2B)**: High-performing with a completion time of **1m:32s**, focusing on efficiency. (Pass)

5. **Visual Language Tasks**:
   - **LLaVA**: Ideal for tasks involving visual interpretation, completing in **2m:31s**. (Pass)

6. **High Detail Requirements**:
   - **Solar**: Offers extensive detail with a longer response time of **4m**. (Pass)

7. **Uncensored Outputs**:
   - **Llama 2 Uncensored**: Use this model for unrestricted responses, completing in **2m:48s**. (Pass)

8. **Reinforcement Learning Applications**:
   - **Starling**: Best for applications leveraging reinforcement learning, with a completion time of **2m:50s**. (Pass)

### Additional Notes
- **Caching**: GitHub Actions uses caching to speed up subsequent runs by storing dependencies.
- **Customization**: You can extend the list of models or adjust the commands as needed.
- **Limitations**: Response time may be impacted by server availability, and larger models may require more processing time.
