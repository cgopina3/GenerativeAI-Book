# Hands-On Exercise: Single-Input Linear Regression with Gradient Descent

## Objective
Learn how to implement a simple linear regression model using **manual gradient descent**. Observe how weights and bias update over multiple epochs to reduce error.

## Dataset
- Input `x = [0.1, 0.2, 0.5, 0.7]`  
- Output `y = [0.3, 0.45, 0.6, 0.10]`

## Initial Parameters
- Weight `w = 0.70`  
- Bias `b = 0.1`  
- Learning rate `alpha = 0.1`

## Steps Implemented
1. **Forward Pass**: Compute predictions using `y_pred = w*x + b`  
2. **Compute 1/2 MSE**:  
   \[
   \text{MSE} = \frac{1}{2n} \sum (y_i - \hat{y}_i)^2
   \]  
3. **Compute Gradients**:  
   - Gradient w.r.t weight: \( \frac{\partial E}{\partial w} = -\sum (y_i - \hat{y}_i) x_i \)  
   - Gradient w.r.t bias: \( \frac{\partial E}{\partial b} = -\sum (y_i - \hat{y}_i) \)  
4. **Average Gradients**: Take mean over all samples  
5. **Update Parameters**:  
   \[
   w := w - \alpha \cdot \text{avg\_grad\_w}, \quad
   b := b - \alpha \cdot \text{avg\_grad\_b}
   \]  
6. Repeat for multiple epochs and observe how the 1/2 MSE decreases.

## How to Run
```bash
python linear_regression_gd.py
