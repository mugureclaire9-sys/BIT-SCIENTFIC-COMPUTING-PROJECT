
import numpy as np
from scipy.interpolate import interp1d

# Original data
x = np.array([1, 2, 3, 4, 5])
y = np.array([10, 20, 30, 40, 50])

linear_function = interp1d(x, y)

print("ORIGINAL RESULTS")
print("Estimated value at x = 2.5:", float(linear_function(2.5)))
print("Estimated value at x = 3.5:", float(linear_function(3.5)))

# Modified data
y_new = np.array([10, 25, 35, 45, 55])

new_function = interp1d(x, y_new)

print("\nMODIFIED RESULTS")
print("Estimated value at x = 2.5:", float(new_function(2.5)))
print("Estimated value at x = 3.5:", float(new_function(3.5)))
