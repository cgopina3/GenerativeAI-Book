import numpy as np
from scipy.stats import norm, binom

# -----------------------------
# Problem 1: From Data to Probability
# -----------------------------
print("=== Problem 1: Data to Probability ===")

# Simulate 100 exam scores between 50 and 100
np.random.seed(42)
exam_scores = np.random.randint(50, 101, 100)

# Step 1: Sample mean and variance
sample_mean = exam_scores.mean()
sample_var = exam_scores.var()
print("Sample Mean:", sample_mean)
print("Sample Variance:", sample_var)

# Step 2: Probability a student scored above 80
prob_above_80 = 1 - norm.cdf(80, loc=sample_mean, scale=np.sqrt(sample_var))
print("P(score > 80):", prob_above_80)
print("Run this code and interpret the probability compared to the data.\n")

# -----------------------------
# Problem 2: Law of Large Numbers
# -----------------------------
print("=== Problem 2: Law of Large Numbers ===")

# Small number of coin flips
flips_10 = np.random.choice([0,1], size=10)
rel_freq_10 = flips_10.mean()
print("10 coin flips, relative frequency of heads:", rel_freq_10)

# Large number of coin flips
flips_10000 = np.random.choice([0,1], size=10000)
rel_freq_10000 = flips_10000.mean()
print("10,000 coin flips, relative frequency of heads:", rel_freq_10000)
print("Observe how frequency stabilizes as number of flips increases.\n")

# -----------------------------
# Problem 3: Understanding Parameters
# -----------------------------
print("=== Problem 3: Standard Error ===")

population_mu = 7000
population_sigma = 1000
n = 50

# Standard error of the mean
sem = population_sigma / np.sqrt(n)
print("Population Std Dev:", population_sigma)
print("Standard Error of the Mean (n=50):", sem)
print("Run and compare SEM to population sigma.\n")

# -----------------------------
# Problem 4: Normal Distribution Application
# -----------------------------
print("=== Problem 4: Normal Probabilities ===")

mu_height = 175
sigma_height = 7

# P(man taller than 185)
prob_taller_185 = 1 - norm.cdf(185, loc=mu_height, scale=sigma_height)
print("P(height > 185 cm):", prob_taller_185)

# Height cutoff for tallest 5%
height_95th = norm.ppf(0.95, loc=mu_height, scale=sigma_height)
print("Height cutoff for top 5%:", height_95th)

# Sample mean > 178 for n=49
n_sample = 49
sem_sample = sigma_height / np.sqrt(n_sample)
prob_sample_mean_178 = 1 - norm.cdf(178, loc=mu_height, scale=sem_sample)
print("P(sample mean > 178 cm, n=49):", prob_sample_mean_178)
print("Run and interpret these probabilities in context.\n")

# -----------------------------
# Problem 5: Real-World Decision Making (Netflix)
# -----------------------------
print("=== Problem 5: Binomial and Normal Approximation ===")

p = 0.7  # probability of finishing the season
n_small = 10
n_large = 100

# Probability exactly 7 finish out of 10
prob_7_out_of_10 = binom.pmf(7, n_small, p)
print("P(exactly 7 finish out of 10):", prob_7_out_of_10)

# Normal approximation for 100 users
mean_large = n_large * p
std_large = np.sqrt(n_large * p * (1-p))
print("For n=100, Normal approximation can be used with mean =", mean_large, "and std dev =", std_large)
print("Observe how Normal approximation simplifies large-sample calculations.\n")

print("DON'T LOOK AT ANSWERS: Run each section, interpret results, and connect them to probability models and inference!")
