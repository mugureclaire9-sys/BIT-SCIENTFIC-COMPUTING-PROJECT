
import numpy as np

# Original polynomial: x^2 - 5x + 6 = 0
coefficients = [1, -5, 6]

print("ORIGINAL RESULTS")

roots = np.roots(coefficients)

print("Polynomial roots:", np.round(roots, 3))

# Modified polynomial: x^2 - 6x + 8 = 0
new_coefficients = [1, -6, 8]

print("\nMODIFIED RESULTS")

new_roots = np.roots(new_coefficients)

print("Modified polynomial roots:", np.round(new_roots, 3))
