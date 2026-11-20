
import numpy as np
from scipy.optimize import curve_fit

# Straight-line function
def linear_model(x, a, b):
    return a * x + b

# Original data
x = np.array([1, 2, 3, 4, 5], dtype=float)
y = np.array([3, 5, 7, 9, 11], dtype=float)

print("ORIGINAL RESULTS")

parameters, _ = curve_fit(linear_model, x, y)

a, b = parameters

print("Slope:", round(a, 2))
print("Intercept:", round(b, 2))
print("Predicted value at x = 6:", round(linear_model(6, a, b), 2))

# Modified data
y_new = np.array([4, 7, 10, 13, 16], dtype=float)

print("\nMODIFIED RESULTS")

new_parameters, _ = curve_fit(linear_model, x, y_new)

new_a, new_b = new_parameters

print("Slope:", round(new_a, 2))
print("Intercept:", round(new_b, 2))
print("Predicted value at x = 6:", round(linear_model(6, new_a, new_b), 2))
