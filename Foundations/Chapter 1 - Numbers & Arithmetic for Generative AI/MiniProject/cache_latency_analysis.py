import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# ===== Example lmbench data (replace with your measured data) =====
memory_size_kb = np.array([1, 2, 4, 8, 16, 32, 64])  # KB
latency_ns = np.array([1.1, 1.2, 1.3, 2.5, 5.8, 12.0, 30.0])  # ns

# ===== Plot latency vs memory size =====
plt.figure(figsize=(8,5))
plt.plot(memory_size_kb, latency_ns, 'o-', label='Measured Latency')
plt.xlabel("Memory Size (KB)")
plt.ylabel("Latency (ns)")
plt.title("Cache Latency vs Memory Size")
plt.grid(True)

# ===== Fit exponential curve =====
def exp_func(x, a, b):
    return a * np.exp(b * x)

params, _ = curve_fit(exp_func, memory_size_kb, latency_ns)
a, b = params
plt.plot(memory_size_kb, exp_func(memory_size_kb, a, b), 'r--', label=f'Fit: {a:.2f}·e^({b:.2f}·x)')
plt.legend()
plt.savefig("cache_plot.png")   # save plot as image
plt.show()

print(f"Fitted exponential: Latency ≈ {a:.2f} * e^({b:.2f} * Size)")
