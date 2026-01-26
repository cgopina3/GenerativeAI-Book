# Lab 3.13: The Lab Notebook—From Theory to Simulation

This lab bridges the gap between statistical theory and practical simulation using Python.

## Overview

In this lab, we:

* Validate the normality of real-world data (human heights).
* Simulate stock market returns using a log-normal distribution.
* Explore the Central Limit Theorem by comparing Binomial and Normal distributions.

## Tasks

### 1. Validating Reality: Heights Experiment

* Calculate sample mean and standard deviation.
* Plot a histogram of the heights with a theoretical normal curve overlay.
* Perform the Kolmogorov-Smirnov (K-S) test to assess normality.
* Success Criteria: p-value > 0.05 indicates data is likely normal.

### 2. Simulating the Market: Log-Normal Returns & VaR

* Generate 10,000 simulated stock prices using a log-normal model.
* Calculate 1% and 5% Value-at-Risk (VaR) percentiles.
* Note: VaR does not capture extreme "Black Swan" events.

### 3. The Great Transformation: Binomial vs. Normal

* Simulate Binomial distributions for different n (10, 30, 100) with p=0.5.
* Observe how the distribution becomes smoother and approximates a Normal distribution as n increases.
* Demonstrates the Central Limit Theorem in practice.

## Note on Code

All Python code to perform these tasks is provided in a separate file: `lab_3_13_code.py`. This README focuses on conceptual explanations and workflow guidance.

## References & Resources

* Dataset: `heights.csv` (Adapted from CDC NHANES)
* Statistics: "All of Statistics" by Larry Wasserman
* Simulation Methods: "Simulation" by Sheldon Ross, 5th Edition
* Python Libraries: SciPy, NumPy, Matplotlib, Seaborn
