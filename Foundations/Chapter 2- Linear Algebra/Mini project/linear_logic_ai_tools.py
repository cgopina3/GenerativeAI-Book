import numpy as np
import matplotlib.pyplot as plt

# -------------------- Part 1: Image Processing --------------------
# Load image
image = plt.imread('sample_image.jpg')

# Convert to grayscale if needed
if image.ndim == 3:
    image_gray = image.mean(axis=2)
else:
    image_gray = image

# Normalize pixel values
image_gray = image_gray / 255.0

# Display original image
plt.imshow(image_gray, cmap='gray')
plt.title("Original Grayscale Image")
plt.axis('off')
plt.show()

# Define a simple edge detection kernel
edge_kernel = np.array([
    [-1, -1, -1],
    [-1,  8, -1],
    [-1, -1, -1]
])

# Convolution function
def apply_filter(image_matrix, kernel):
    pad_width = kernel.shape[0] // 2
    padded_image = np.pad(image_matrix, pad_width, mode='constant', constant_values=0)
    filtered_image = np.zeros_like(image_matrix)

    for i in range(filtered_image.shape[0]):
        for j in range(filtered_image.shape[1]):
            neighborhood = padded_image[i:i+kernel.shape[0], j:j+kernel.shape[1]]
            filtered_image[i, j] = np.sum(neighborhood * kernel)
    
    filtered_image = np.clip(filtered_image, 0, 1)
    return filtered_image

# Apply edge filter
filtered_image = apply_filter(image_gray, edge_kernel)

# Display filtered image
plt.imshow(filtered_image, cmap='gray')
plt.title("Edge Detected Image")
plt.axis('off')
plt.show()

# Optional: Image rotation (bonus)
theta = np.radians(15)
rotation_matrix = np.array([
    [np.cos(theta), -np.sin(theta)],
    [np.sin(theta),  np.cos(theta)]
])

# -------------------- Part 2: Movie Recommender System --------------------
# User-Movie Ratings Matrix
ratings = np.array([
    [5, 0, 3, 0],  # User 1
    [0, 3, 0, 5],  # User 2
    [1, 0, 5, 0],  # User 3
    [0, 3, 0, 4],  # User 4
    [4, 0, 2, 0]   # User 5
])

users = ['User1','User2','User3','User4','User5']
movies = ['Movie A','Movie B','Movie C','Movie D']

print("Ratings Matrix:\n", ratings)

# Cosine similarity function
def calculate_similarity(u1, u2):
    common_mask = (u1 != 0) & (u2 != 0)
    if np.sum(common_mask) == 0:
        return 0
    u1_common = u1[common_mask]
    u2_common = u2[common_mask]
    return np.dot(u1_common, u2_common) / (np.linalg.norm(u1_common) * np.linalg.norm(u2_common))

# Recommendation function
def recommend_movies(target_user_id, ratings_matrix, num_recommendations=2):
    similarities = []
    for i in range(ratings_matrix.shape[0]):
        if i != target_user_id:
            sim = calculate_similarity(ratings_matrix[target_user_id], ratings_matrix[i])
            similarities.append((i, sim))
    similarities.sort(key=lambda x: x[1], reverse=True)
    top_users = [x[0] for x in similarities[:2]]
    
    pred_ratings = []
    for j in range(ratings_matrix.shape[1]):
        if ratings_matrix[target_user_id, j] == 0:
            weighted_sum = sum(ratings_matrix[u, j]*calculate_similarity(ratings_matrix[target_user_id], ratings_matrix[u]) for u in top_users)
            total_weight = sum(calculate_similarity(ratings_matrix[target_user_id], ratings_matrix[u]) for u in top_users)
            pred_ratings.append((movies[j], weighted_sum/total_weight if total_weight != 0 else 0))
    
    pred_ratings.sort(key=lambda x: x[1], reverse=True)
    return pred_ratings[:num_recommendations]

# Example: Recommendations for User1
recommendations = recommend_movies(0, ratings)
print("Recommendations for User1:", recommendations)

# Optional: Truncated SVD
U, s, Vt = np.linalg.svd(ratings, full_matrices=False)
k = 2
U_k = U[:, :k]
s_k = s[:k]
Vt_k = Vt[:k, :]
reconstructed_ratings = np.dot(U_k, np.dot(np.diag(s_k), Vt_k))
print("SVD Reconstructed Ratings Matrix:\n", np.round(reconstructed_ratings, 2))
