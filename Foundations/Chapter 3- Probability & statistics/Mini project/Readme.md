# Practical Lab: Visualizing Goodness of Fit in Python

This lab demonstrates how to visualize the goodness of fit for normally distributed data, including the effects of outliers.

## Overview
We will generate a synthetic dataset representing daily coffee consumption, add a few outliers, and analyze the data using histograms, KDEs, Q-Q plots, and the 3-sigma rule.

## 1. Setup
Import the necessary libraries for statistical analysis and visualization.

## 2. Generating the Data
We create 1,000 normal data points and add a few extreme outliers.

## 3. Visualizing Histogram and KDE
Overlay the histogram and KDE with the theoretical normal curve to see how the data distribution compares to a perfect normal.

**Observation:** The KDE follows the data, but the normal curve is affected by the outliers.

## 4. Q-Q Plot
Use a Q-Q plot to assess normality.

**Insight:** Most points lie on the line, but outliers lift off the top right, indicating heavy right tails.

## 5. Identifying Outliers (3-Sigma Rule)
Outliers are detected using the 3-sigma rule, which flags any data point beyond 3 standard deviations from the mean.

## Note on Code
All the code used to generate, visualize, and analyze the data is provided in a separate Python file (`coffee_outliers_code.py`). This README focuses on explanations, observations, and workflow guidance.

---
This workflow can be used for automated anomaly detection, statistical quality control, or understanding the distribution of real-world data.

