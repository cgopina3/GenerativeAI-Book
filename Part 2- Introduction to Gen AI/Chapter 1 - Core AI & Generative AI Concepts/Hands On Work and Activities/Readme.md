# Hands-On Activities: Core AI & Generative AI Concepts

This document outlines a set of practical exercises to reinforce understanding of AI models, prompt engineering, and generative techniques.

## 1. Prompt Engineering for Chess Puzzles
- Use an LLM (e.g., ChatGPT, Claude, Gemini) to:
  - Generate three chess puzzles: Easy, Medium, Hard.
  - Ask the AI to explain the solution step-by-step.
  - Refine prompts to create diverse puzzle patterns (fork, pin, skewer, checkmate, discovered attack).

## 2. Compare Modern LLMs
- Research the following models: GPT-3, GPT-4, LLaMA, PaLM, Claude.
- Create a table with the columns:
  | Model | Release Year | Parameters | Key Innovations | Primary Applications |
- Fill in the table using reliable sources.

## 3. Compare Generative Architectures
- Create a table with columns:
  | Model Type | Used For | Advantages | Disadvantages | Example Use Case |
- Include GAN, VAE, Transformer, Diffusion models and their characteristics.

## 4. Discriminative vs. Generative Classification Exercise
- Discriminative Task:
  - Provide an animal description (e.g., “An animal with stripes that lives in the savannah”).
  - Ask the LLM to classify it (X → Y).
- Generative Task:
  - Ask the model to generate a new animal description with similar traits (Y → X).
- Write a short reflection comparing the reasoning approaches.

## 5. Latent Space Exploration (VAE Analogy Exercise)
- Pick any object (car, phone, fruit, animal).
- List essential features (cannot change identity) and variable features (color, size, shape, texture).
- Explain how changing variable features creates a new “sample,” analogous to latent-space variation.

### Example:
- Object: Car
  - Essential: wheels, engine, body shape
  - Variable: color, size, interior design
  - New sample: “blue compact car instead of a red sedan”

## Note on Implementation
These exercises can be completed interactively using Python notebooks or AI tools. Code can be organized in a separate file `hands_on_activities.py` if applicable.