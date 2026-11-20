
import numpy as np

def jacobi_method(A, B, tolerance=1e-6, max_iterations=1000):
    n = len(B)
    x = np.zeros(n)

    for iteration in range(1, max_iterations + 1):
        new_x = np.zeros(n)

        for i in range(n):
            sum_values = 0

            for j in range(n):
                if i != j:
                    sum_values += A[i][j] * x[j]

            new_x[i] = (B[i] - sum_values) / A[i][i]

        if np.linalg.norm(new_x - x, ord=np.inf) < tolerance:
            return new_x, iteration

        x = new_x

    return x, max_iterations


A = np.array([
    [10, 1, 1],
    [2, 10, 1],
    [2, 2, 10]
], dtype=float)

B = np.array([12, 13, 14], dtype=float)

print("ORIGINAL RESULTS")
solution, iterations = jacobi_method(A, B)
print("Solution:", np.round(solution, 3))
print("Iterations:", iterations)

# Modified input
B_new = np.array([13, 13, 14], dtype=float)

print("\nMODIFIED RESULTS")
new_solution, new_iterations = jacobi_method(A, B_new)
print("Solution:", np.round(new_solution, 3))
print("Iterations:", new_iterations)
