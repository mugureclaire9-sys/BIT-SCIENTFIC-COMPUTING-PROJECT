
import numpy as np

A = np.array([
    [4, 1],
    [2, 3]
], dtype=float)

print("ORIGINAL RESULTS")

eigenvalues, eigenvectors = np.linalg.eig(A)

print("Eigenvalues:")
print(np.round(eigenvalues, 3))

print("Eigenvectors:")
print(np.round(eigenvectors, 3))

# Modified input
A_new = np.array([
    [5, 1],
    [2, 3]
], dtype=float)

print("\nMODIFIED RESULTS")

new_eigenvalues, new_eigenvectors = np.linalg.eig(A_new)

print("Eigenvalues:")
print(np.round(new_eigenvalues, 3))

print("Eigenvectors:")
print(np.round(new_eigenvectors, 3))
