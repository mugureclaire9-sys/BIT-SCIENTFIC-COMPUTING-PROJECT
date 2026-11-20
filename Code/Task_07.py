
import numpy as np
from scipy.linalg import lu_factor, lu_solve

A = np.array([
    [2, 1, 1],
    [1, 3, 2],
    [1, 0, 0]
], dtype=float)

B = np.array([7, 13, 1], dtype=float)


def gaussian_elimination(A, B):
    matrix = np.column_stack((A.copy(), B.copy()))
    n = len(B)

    # Forward elimination
    for i in range(n):
        for j in range(i + 1, n):
            factor = matrix[j, i] / matrix[i, i]
            matrix[j] = matrix[j] - factor * matrix[i]

    # Back substitution
    x = np.zeros(n)

    for i in range(n - 1, -1, -1):
        x[i] = (
            matrix[i, -1] -
            np.dot(matrix[i, i + 1:n], x[i + 1:n])
        ) / matrix[i, i]

    return x


print("ORIGINAL RESULTS")

gaussian_solution = gaussian_elimination(A, B)
print("Gaussian elimination:", np.round(gaussian_solution, 2))

lu, piv = lu_factor(A)
lu_solution = lu_solve((lu, piv), B)
print("LU decomposition:", np.round(lu_solution, 2))

# Modified input
B_new = np.array([8, 13, 1], dtype=float)

print("\nMODIFIED RESULTS")

new_gaussian = gaussian_elimination(A, B_new)
print("Gaussian elimination:", np.round(new_gaussian, 2))

new_lu = lu_solve((lu, piv), B_new)
print("LU decomposition:", np.round(new_lu, 2))
