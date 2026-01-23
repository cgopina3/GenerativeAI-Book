# Foundations Mini Projects – Generative AI Book

This chapter contains three foundational computing mini-projects demonstrating important concepts in programming, numerical computation, and computer architecture.

---

## 1. Machine Epsilon (Python)

### Problem Statement
Find the **smallest positive floating-point number** ε such that:

```
1.0 + ε != 1.0
```

### Concept
- Floating-point precision  
- Machine epsilon  
- Iterative brute-force approach

### Solution
Implemented in [`machine_epsilon.py`](machine_epsilon.py)

### How to Run
```bash
python machine_epsilon.py
```

### Sample Output
```
Machine epsilon: 2.220446049250313e-16
1.0 + eps = 1.0000000000000002
1.0 + eps/2 = 1.0
```

---

## 2. 255 + 1 Overflow (JavaScript)

### Problem Statement
Demonstrate **overflow** of an 8-bit unsigned integer when adding 1 to 255.

### Concept
- Unsigned 8-bit integer (0–255)  
- Overflow wraps around modulo 256  
- Use `Uint8Array` in JavaScript

### Solution
Implemented in [`uint8_overflow.js`](uint8_overflow.js)

### How to Run
```bash
node uint8_overflow.js
```

### Output
```
0
```

**Explanation:**  
Adding 1 to 255 in an 8-bit unsigned integer wraps around to 0 because `Uint8Array` stores only 0–255 values.

---

## 3. Cache Latency vs Memory Size (Python)

### Problem Statement
Measure **memory latency** for different cache levels (L1, L2, L3) and main memory, then fit an **exponential curve** to the latency data.

### Concept
- Cache hierarchy: L1 → L2 → L3 → RAM  
- Latency increases with memory size  
- Exponential growth model:  
```
Latency ≈ a * e^(b * Size)
```

### Solution
Implemented in [`cache_latency_analysis.py`](cache_latency_analysis.py)

### How to Run
```bash
python cache_latency_analysis.py
```

### LMbench Guide
To obtain real latency measurements, follow these steps:
1. **Install lmbench**:
   - Linux: `sudo apt-get install lmbench`
   - Mac: `brew install lmbench`
   - Windows: Use WSL or a Linux VM
2. **Run memory latency test**:
   ```bash
   cd /usr/lib/lmbench/bin
   ./lat_mem_rd 128 4096
   ```
   - `128` → stride in bytes
   - `4096` → memory size in KB
3. **Save results** in a CSV or directly in the Python script.
4. **Replace example arrays** in `cache_latency_analysis.py` with your measurements:
   ```python
   memory_size_kb = [1,2,4,8,16,32,64]
   latency_ns = [1.1,1.2,1.3,2.5,5.8,12.0,30.0]
   ```
5. **Run the script** to generate the plot and exponential fit.

### Notes
- The script generates a **latency vs memory size plot** (`cache_plot.png`) and prints the **exponential fit formula**.  
- Replace example data with your actual `lmbench` measurements.  
- The plot visually demonstrates jumps in latency when moving from one cache level to the next.

---

## Summary

| Mini Project | Language | Concept | File |
|-------------|---------|---------|------|
| Machine Epsilon | Python | Floating-point precision | `machine_epsilon.py` |
| 255 + 1 Overflow | JavaScript | Integer overflow / Uint8Array | `uint8_overflow.js` |
| Cache Latency | Python | Cache memory, exponential fit | `cache_latency_analysis.py` |

Each project is **self-contained**, and the code can be run independently. This structure ensures clarity and reproducibility for all three mini-projects.

