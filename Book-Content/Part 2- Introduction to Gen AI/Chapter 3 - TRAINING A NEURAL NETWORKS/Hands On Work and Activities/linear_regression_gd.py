# linear_regression_gd.py
# Hands-On Exercise: Single-Input Linear Regression using Gradient Descent

# Input data
x = [0.1, 0.2, 0.5, 0.7]
y = [0.3, 0.45, 0.6, 0.10]

# Initial parameters
w = 0.70  # weight
b = 0.1   # bias
alpha = 0.1  # learning rate

# Number of epochs
epochs = 10

print("Epoch |   Weight   |   Bias   |   1/2 MSE")
print("------------------------------------------")

for epoch in range(epochs):
    # Forward Pass: compute predictions
    y_pred = [w * xi + b for xi in x]

    # Compute 1/2 Mean Squared Error
    errors = [yi - ypi for yi, ypi in zip(y, y_pred)]
    mse = 0.5 * sum(e**2 for e in errors) / len(x)

    # Compute Gradients
    grad_w = [-e * xi for e, xi in zip(errors, x)]
    grad_b = [-e for e in errors]

    # Average Gradients
    avg_grad_w = sum(grad_w) / len(x)
    avg_grad_b = sum(grad_b) / len(x)

    # Update Parameters
    w = w - alpha * avg_grad_w
    b = b - alpha * avg_grad_b

    print(f"{epoch+1:3d}   | {w:8.4f} | {b:6.4f} | {mse:8.4f}")
