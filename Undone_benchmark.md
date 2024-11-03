# Undone Benchmark for LLM

## Introduction

This document serves to clarify the current status of the benchmark for the Large Language Model (LLM) under evaluation. As of now, the benchmark is incomplete and not ready for formal reporting or analysis.

## Current Status

- **Benchmark Design**: The design phase of the benchmark is still in progress. Key performance indicators (KPIs) and evaluation metrics are being refined.
  
- **Data Collection**: The necessary datasets for benchmarking have not yet been fully gathered. Ongoing efforts are being made to source high-quality and relevant data.

- **Testing Procedures**: Formal testing procedures have not been established. Once the design and data collection are complete, a systematic approach to testing will be developed.

- **Results Compilation**: No results have been generated yet. Consequently, there are no findings or insights to report at this time.

## Next Steps

```markdown
# LLM Benchmark Instructions

## Overview

This benchmark is designed to evaluate Large Language Models (LLMs) by gauging their responses to a specific Python script containing errors. Each model will be tested to identify issues and propose fixes. The results will be recorded, including the model name, test details, completion time, and any additional notes.

## Benchmark Details

### Script to Test

Below is the Python script that models will be evaluated against:

```python
def calculate_area(radius):
    pi = 3.14
    area = pi * radius * radius
    return area

def main():
    r = input("Enter the radius: ")
    area = calculate_area(r)
    print("The area of the circle is: " + area)

if __name__ == "__main__":
    main()
```

### Instructions for Models

1. **Identify Errors**: Each model must list all the errors found in the script.
2. **Provide Fixes**: After identifying the errors, the model should rewrite the code correctly.

### Expected Output Format

The output from each model should be structured as follows:

- **Errors Found**: 
    - Error 1: Description
    - Error 2: Description
    - (and so on...)

- **Corrected Code**:
    ```python
    # Corrected version of the script goes here
    ```

## Results Storage

All runs, identified issues, and proposed fixes will be documented in a table format in the README. The table will include the following columns:

| Model Name | Test Description | Completion Time | Notes |
|------------|------------------|------------------|-------|
| Model A    | Error list and fix for provided script | X seconds | Additional notes if necessary |
| Model B    | Error list and fix for provided script | Y seconds | Additional notes if necessary |

## Fact based benchmark

---

# Fact-Based Reasoning Benchmark

## Instructions for the Model
- You will be presented with a series of factual questions.
- Your response should begin with "Yes" or "No" (if applicable), followed by a clear and concise explanation that elaborates on your answer.
- Ensure each response is accurate and provides context or necessary details to fully explain the fact.

---

## Fact-Converted Question Table
| **Fact** | **Converted Question** | **Answer** |
|-----------|------------------------|------------|
| Australia is wider than the moon | Is Australia wider than the moon? | Yes, Australia is wider than the moon. Australia is almost 4,000 km in diameter from east to west, while the moon is 3,400 km in diameter. |
| Cows are sacred in Hinduism | Are cows considered sacred in Hinduism? | Yes, cows are considered sacred in Hinduism. Their products, such as milk, urine, and dung, are highly valued, and eating cow meat is taboo. |
| Avocados are technically a fruit | Are avocados technically classified as a fruit? | Yes, avocados are technically a fruit. They meet the botanical criteria for a berry, having a large seed and fleshy pulp. |
| Bats are the only flying mammals | Are bats the only mammals that can truly fly? | Yes, bats are the only flying mammals. While flying squirrels can glide, they do not have the ability to sustain powered flight. |
| Earth's magnetic pole moves westward | Does Earth's magnetic north pole move over time? | Yes, Earth's magnetic north pole moves, unlike the geographic North Pole, which remains fixed. |
| Forests produce rainfall | Do forests contribute to rainfall production? | Yes, forests produce rainfall. Trees release water vapor through a process called transpiration, forming clouds and contributing to rainfall. |
| Ketchup was once sold as medicine | Was ketchup once sold as medicine? | Yes, in the 1830s, tomato ketchup was sold as a medicine to treat ailments like diarrhea, jaundice, and indigestion. |
| Nutmeg is a hallucinogen | Can consuming nutmeg cause hallucinations? | Yes, nutmeg can cause hallucinations, convulsions, seizures, and a type of "nutmeg psychosis" when consumed in large quantities. |
| The moon experiences moonquakes | Does the moon experience moonquakes? | Yes, the moon experiences moonquakes, some of which are strong enough to move furniture. The moon's rock continues to vibrate longer than Earth's rock during earthquakes. |

---

## Full Benchmark Questions
1. **Is Australia wider than the moon?**
   - **Expected Answer**: "Yes, Australia is wider than the moon. Australia is almost 4,000 km in diameter from east to west, while the moon is 3,400 km in diameter."

2. **Are cows considered sacred in Hinduism?**
   - **Expected Answer**: "Yes, cows are considered sacred in Hinduism. Their products, such as milk, urine, and dung, are highly valued, and eating cow meat is taboo."

3. **Are avocados technically classified as a fruit?**
   - **Expected Answer**: "Yes, avocados are technically a fruit. They meet the botanical criteria for a berry, having a large seed and fleshy pulp."

4. **Are bats the only mammals that can truly fly?**
   - **Expected Answer**: "Yes, bats are the only flying mammals. While flying squirrels can glide, they do not have the ability to sustain powered flight."

5. **Does Earth's magnetic north pole move over time?**
   - **Expected Answer**: "Yes, Earth's magnetic north pole moves, unlike the geographic North Pole, which remains fixed."

6. **Do forests contribute to rainfall production?**
   - **Expected Answer**: "Yes, forests produce rainfall. Trees release water vapor through a process called transpiration, forming clouds and contributing to rainfall."

7. **Was ketchup once sold as medicine?**
   - **Expected Answer**: "Yes, in the 1830s, tomato ketchup was sold as a medicine to treat ailments like diarrhea, jaundice, and indigestion."

8. **Can consuming nutmeg cause hallucinations?**
   - **Expected Answer**: "Yes, nutmeg can cause hallucinations, convulsions, seizures, and a type of 'nutmeg psychosis' when consumed in large quantities."

9. **Does the moon experience moonquakes?**
   - **Expected Answer**: "Yes, the moon experiences moonquakes, some of which are strong enough to move furniture. The moon's rock continues to vibrate longer than Earth's rock during earthquakes."

---

## External Example
- **Question**: "Is Mount Everest the highest mountain in the world?"
- **How the Model Should Answer**: 
  - **Example Answer**: "Yes, Mount Everest is the highest mountain in the world. It stands at 8,848 meters (29,029 feet) above sea level, making it the tallest peak globally."

This external example illustrates how the model should format its response, providing a comprehensive yet straightforward explanation. 

---

This file structure will ensure that the LLM’s responses are organized, factually accurate, and formatted in a consistent manner for easy assessment and evaluation.
```
