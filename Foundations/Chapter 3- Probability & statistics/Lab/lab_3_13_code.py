import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import ks_1samp, norm, binom

# 1️⃣ Height Analysis – Validate Normality
# Load the data
data = pd.read_csv('heights.csv')['Height']  # Replace 'Height' with your column name if different

# Step 1: Compute mean and standard deviation
sample_mean = data.mean()
sample_std = data.std()
print("Sample Mean:", sample_mean)
print("Sample Std Dev:", sample_std)

# Step 2: Histogram with Normal overlay
x = np.linspace(min(data), max(data), 100)
plt.hist(data, bins=20, density=True, alpha=0.6, color='skyblue', edgecolor='black')
plt.plot(x, norm.pdf(x, sample_mean, sample_std), color='red', lw=2)
plt.title('Histogram with Normal Overlay')
plt.show()

# Step 3: K-S test
ks_stat, p_value = ks_1samp(data, lambda x: norm.cdf(x, sample_mean, sample_std))
print("K-S Statistic:", ks_stat)
print("p-value:", p_value)
print("\nDON'T LOOK AT THE ANSWERS: Run this code and interpret whether the data is likely Normal!")

# 2️⃣ Stock Simulation – Log-Normal Returns & VaR
# Parameters
mu = 0.001      # daily return mean
sigma = 0.02    # daily return std dev
S0 = 100        # initial stock price
days = 252      # trading days in a year
simulations = 10000

# Monte Carlo simulation of stock prices
np.random.seed(42)  # for reproducibility
returns = np.random.lognormal(mean=mu, sigma=sigma, size=(simulations, days))
price_paths = S0 * returns.cumprod(axis=1)  # simulate stock price path

# Extract final day prices
final_prices = price_paths[:, -1]

# Calculate VaR
VaR_1 = np.percentile(final_prices, 1)
VaR_5 = np.percentile(final_prices, 5)
print("1% VaR:", VaR_1)
print("5% VaR:", VaR_5)
print("\nDON'T LOOK AT THE ANSWERS: Run this code and interpret the 1% and 5% VaR!")

# 3️⃣ Binomial vs. Normal – Central Limit Theorem
p = 0.5  # probability of success

for n in [10, 30, 100]:
    k = np.arange(0, n+1)
    binom_probs = binom.pmf(k, n, p)
    
    # Plot Binomial
    plt.bar(k, binom_probs, alpha=0.6, label=f'Binomial n={n}')
    
    # Normal approximation
    mean = n * p
    std = np.sqrt(n * p * (1-p))
    plt.plot(k, norm.pdf(k, mean, std), 'r-', lw=2, label='Normal approx')
    
    plt.title(f'Binomial vs Normal (n={n})')
    plt.xlabel('Number of successes')
    plt.ylabel('Probability')
    plt.legend()
    plt.show()

print("DON'T LOOK AT THE ANSWERS: Run this code and observe how the Binomial distribution smooths as n increases.")