# Inventory-Opt-LLM
A comparison between Large Language Models for Inventory Optimization

## Tasks
1. Test if Large Language Models are able to generate bayesian networks.
2. Test if Large Language Models are able to generate proper results with correct reasoning given
different types of prompting strategies:
   1. Zero Shot Prompting 
   2. Few Shot Prompting

## Strategy
- Task 1
  - Provide some background context to the LLMs by asking generic questions.
  - Using the background ask the LLMs to generate a bayesian network.
  - Ask LLMs to generate a corresponding model in Python with visualization capability.

- Task 2
  - Provide prompts to the LLMs for test (zero shot).
  - Provide prompts to the LLMs for training (few shot) and a new test case.

## Results
- A lot of the analysis has been done manually. It would be better to generate automated analysis measures.
- GPT-3.5 performs a lot better than BARD in both tasks however in some cases both models perform well.