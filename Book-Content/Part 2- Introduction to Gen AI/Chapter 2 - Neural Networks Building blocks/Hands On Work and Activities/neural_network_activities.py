import numpy as np
import matplotlib.pyplot as plt

# -----------------------------
# Activity 3: Forward Pass Function
# -----------------------------
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

def forward_pass(X, W, b):
    z = np.dot(X, W) + b
    y = sigmoid(z)
    return y

# Test
X = np.array([[0.5, 1.0]])
W = np.array([[0.2, 0.8],
              [0.6, -0.4]])
b = np.array([[0.1, -0.2]])
print("Forward Pass Output:", forward_pass(X, W, b))

# -----------------------------
# Activity 4: Plot Loss Curve (XOR Example)
# -----------------------------
# Example XOR training loop with placeholder loss values
epochs = 50
loss_values = np.exp(-0.1*np.arange(epochs))  # dummy decreasing loss

plt.plot(range(epochs), loss_values, marker='o')
plt.title('Loss vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.grid(True)
plt.show()
