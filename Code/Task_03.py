
import numpy as np
import timeit

# Generate 1 million network latency readings
rng = np.random.default_rng(42)
latency_ms = rng.uniform(5, 250, 1_000_000)

# Using a normal Python loop
def loop_version():
    results = []
    for value in latency_ms:
        seconds = value / 1000
        results.append(seconds ** 2)
    return results

# Using NumPy vectorization
def vectorized_version():
    seconds = latency_ms / 1000
    return seconds ** 2

# Measure execution time
loop_time = timeit.timeit(loop_version, number=1)
vector_time = timeit.timeit(vectorized_version, number=3) / 3

# Display results
result = vectorized_version()

print("FIRST FIVE RESULTS:")
print(result[:5])

print("\nEXECUTION TIMES:")
print("Loop time:", round(loop_time, 4), "seconds")
print("Vectorized time:", round(vector_time, 4), "seconds")

print("\nVectorization is faster:",
      vector_time < loop_time)
