import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# -----------------------------
# 1. Load a CSV Dataset
# -----------------------------
# Replace 'dataset.csv' with your actual CSV file
data = pd.read_csv('dataset.csv')
print("Dataset Head:")
print(data.head())
print("\nSummary Statistics:")
print(data.describe())

# -----------------------------
# 2. Create Histograms and Scatter Plots
# -----------------------------
# Histogram of a numeric column (replace 'column_name')
data_column = 'column_name'  # change to a numeric column
plt.hist(data[data_column], bins=20, color='skyblue', edgecolor='black')
plt.title(f'Histogram of {data_column}')
plt.xlabel(data_column)
plt.ylabel('Frequency')
plt.show()

# Scatter plot between two numeric columns (replace 'x_column' and 'y_column')
x_column = 'x_column'
y_column = 'y_column'
plt.scatter(data[x_column], data[y_column], color='green')
plt.title(f'Scatter Plot of {y_column} vs {x_column}')
plt.xlabel(x_column)
plt.ylabel(y_column)
plt.show()

# -----------------------------
# 3. Compute Basic Statistics
# -----------------------------
numbers = [10, 20, 30, 40, 50]  # example list
mean_value = np.mean(numbers)
range_value = np.max(numbers) - np.min(numbers)
print(f"Mean: {mean_value}, Range: {range_value}")

# -----------------------------
# 4. Mini-Project: Collect Class Data and Visualize
# -----------------------------
# Example data: favorite numbers from 10 students
class_data = {'Student': range(1, 11), 'FavoriteNumber': [3,7,1,5,8,2,6,9,4,10]}
class_df = pd.DataFrame(class_data)

# Histogram
plt.hist(class_df['FavoriteNumber'], bins=10, color='orange', edgecolor='black')
plt.title('Histogram of Favorite Numbers')
plt.xlabel('Number')
plt.ylabel('Frequency')
plt.show()

# Scatter plot (Student ID vs Favorite Number)
plt.scatter(class_df['Student'], class_df['FavoriteNumber'], color='purple')
plt.title('Scatter Plot: Student vs Favorite Number')
plt.xlabel('Student')
plt.ylabel('Favorite Number')
plt.show()