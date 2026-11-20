
import numpy as np

# Coefficient matrix
A = np.array([
    [2, 1],
    [1, 3]
])

# Constant values
B = np.array([8, 13])

# Solve the equations
solution = np.linalg.solve(A, B)

print("ORIGINAL RESULTS")
print("x =", solution[0])
print("y =", solution[1])

# Modified input
B_new = np.array([10, 13])

# Solve modified equations
new_solution = np.linalg.solve(A, B_new)

print("\nMODIFIED RESULTS")
print("x =", new_solution[0])
print("y =", new_solution[1])
