# README.md

# Linear Logic: Building Basic AI Tools

## Project Overview
This project demonstrates the application of linear algebra concepts in building foundational AI tools using Python and NumPy. The focus is on two practical applications:

1. **Image Processing**: Implementing convolution-based filters for edge detection.
2. **Movie Recommender System**: Computing user-user similarity and predicting missing ratings using vector operations and optional SVD-based matrix factorization.

This project reinforces the concepts of vectors, matrices, dot products, norms, and linear transformations in the context of real-world AI tasks.

## Features

### Part 1: Image Processing
- Load a grayscale image using `matplotlib.pyplot.imread()`.
- Normalize pixel values to `[0, 1]`.
- Apply a simple edge detection filter using convolution.
- (Optional) Rotate image using a 2x2 rotation matrix.

### Part 2: Movie Recommender System
- Represent user-movie ratings as a matrix.
- Compute cosine similarity between users.
- Generate movie recommendations based on top similar users.
- (Optional) Apply truncated SVD to reconstruct missing ratings.

## Requirements
- Python 3.x
- NumPy
- Matplotlib

Install dependencies using:
```bash
pip install numpy matplotlib
```

## Usage
1. Clone the repository.
2. Place your sample image in the repository folder (e.g., `sample_image.jpg`).
3. Run the Python script:
```bash
python linear_logic_ai_tools.py
```
4. The script will:
   - Display the original grayscale image.
   - Display the filtered edge-detected image.
   - Print the ratings matrix.
   - Print recommendations for a selected user.
   - (Optional) Display SVD reconstructed ratings matrix.

## File Structure
```
linear_logic_ai_tools/
│
├── README.md            # This file
├── linear_logic_ai_tools.py   # Main Python script
├── sample_image.jpg     # Example image for Part 1
```

## Learning Outcomes
- Implement matrix operations and transformations in Python.
- Apply convolution for image filtering.
- Compute user-user similarity and generate recommendations.
- Understand SVD-based matrix factorization for recommender systems.
