import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats

# Set plot style
sns.set_theme(style="whitegrid")

# Generate data
data = np.random.normal(loc=2, scale=0.5, size=1000)
outliers = np.array([5.2, 5.5, 5.8, 6.0, 6.2])
combined_data = np.concatenate([data, outliers])

# Histogram + KDE
plt.figure(figsize=(10, 6))
sns.histplot(combined_data, kde=True, stat="density", color="skyblue", label="Actual Data (Hist + KDE)")
x = np.linspace(min(combined_data), max(combined_data), 100)
plt.plot(x, stats.norm.pdf(x, np.mean(combined_data), np.std(combined_data)), color='red', linestyle='--', label="Theoretical Normal Curve")
plt.title("Histogram with KDE Overlay vs. Normal Curve")
plt.legend()
plt.show()

# Q-Q Plot
plt.figure(figsize=(8, 6))
stats.probplot(combined_data, dist="norm", plot=plt)
plt.title("Q-Q Plot: Checking for Normality")
plt.show()

# 3-Sigma Rule
mean = np.mean(combined_data)
std = np.std(combined_data)
upper_limit = mean + 3 * std
lower_limit = mean - 3 * std
outliers_detected = combined_data[(combined_data > upper_limit) | (combined_data < lower_limit)]

print(f"Mean: {mean:.2f}")
print(f"3-Sigma Upper Limit: {upper_limit:.2f}")
print(f"Outliers detected: {outliers_detected}")