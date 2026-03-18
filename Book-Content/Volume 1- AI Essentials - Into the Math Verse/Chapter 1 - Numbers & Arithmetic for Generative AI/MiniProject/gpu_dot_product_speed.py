import numpy as np
import time

# Define the vector dimension
vector_size = 50000000  # 50 million elements

print(f"Testing with vector size: {vector_size}")

# --- FP32 (Single Precision) Test ---
print("\n--- FP32 (Single Precision) Test ---")
a_fp32 = np.random.rand(vector_size).astype(np.float32)
b_fp32 = np.random.rand(vector_size).astype(np.float32)

start_time = time.time()
result_fp32 = np.dot(a_fp32, b_fp32)
end_time = time.time()
fp32_time = end_time - start_time
print(f"FP32 Dot Product result (first 5 digits): {result_fp32:.5f}")
print(f"FP32 execution time: {fp32_time:.4f} seconds")

# --- FP16 (Half Precision) Test ---
print("\n--- FP16 (Half Precision) Test ---")
a_fp16 = np.random.rand(vector_size).astype(np.float16)
b_fp16 = np.random.rand(vector_size).astype(np.float16)

start_time = time.time()
result_fp16 = np.dot(a_fp16, b_fp16)
end_time = time.time()
fp16_time = end_time - start_time
print(f"FP16 Dot Product result (first 5 digits): {result_fp16:.5f}")
print(f"FP16 execution time: {fp16_time:.4f} seconds")

# --- Comparison ---
print("\n--- Comparison ---")
speedup = fp32_time / fp16_time
print(f"FP16 is approximately {speedup:.2f}x faster than FP32.")
