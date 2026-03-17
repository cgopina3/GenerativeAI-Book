# Hands-On Neural Network Activities

This document outlines practical exercises for understanding neural network forward passes, backpropagation, and coding implementation.

## Activity 1 — Manual Forward Pass Calculation (Single Neuron)
**Given:**
- Input vector: X = [0.5, 0.2]
- Weights: W = [0.8, -0.4]
- Bias: b = 0.1
- Activation: Sigmoid

**Tasks:**
1. Compute the weighted sum: z = X·W + b
2. Compute the activation output: y = sigmoid(z)

**Expected Outcome:**
- Show all steps and calculations by hand.

## Activity 2 — Manual Backpropagation Update (One Output Neuron)
**Given:**
- Input: x1 = 0.3, x2 = 0.9
- Weights (Input→Hidden): w11=0.4, w21=0.2, w12=0.6, w22=0.3
- Weights (Hidden→Output): w13=0.5, w23=0.2
- Biases: 0
- Target: 0.7
- Learning rate: 1

**Tasks:**
1. Forward Pass:
   - Compute hidden layer weighted sums: a1, a2
   - Apply sigmoid to get hidden outputs: y1, y2
   - Compute output layer weighted sum: a3
   - Apply sigmoid to get output: y3
2. Compute output error: E = y_target - y3
3. Backward Pass:
   - Compute output delta δ3
   - Compute hidden deltas δ1, δ2
4. Weight Update:
   - Update weights Input→Hidden and Hidden→Output using δ values
   - Write new weights after update
5. Optional: Perform forward pass with updated weights and compute new output

## Activity 3 — Implement Forward Pass Only (Python Coding Task)
**Task:**
- Write a Python function that performs linear combination and sigmoid activation, returning output.

**Starter Template:**
```python
import numpy as np

def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward_pass(X, W, b):
    # TODO: compute z
    # TODO: compute activation
    # TODO: return output
    pass

# Test with sample values:
X = np.array([[0.5, 1.0]])
W = np.array([[0.2, 0.8],
              [0.6, -0.4]])
b = np.array([[0.1, -0.2]])

print(forward_pass(X, W, b))
```

## Activity 4 — Plot Loss Curve (Using Your XOR Code)
**Task:**
- Modify the training loop to store loss per epoch.
- Plot Loss vs Epoch using matplotlib.
- Observe how the loss decreases during training.

## Note on Implementation
Python code for forward pass, backpropagation, and plotting can be organized in a separate file `neural_network_activities.py`. This README focuses on tasks, calculations, and workflow guidance.

