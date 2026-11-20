import numpy as np
from scipy.integrate import trapezoid

def function(x):
    return x ** 2

# Original input
x = np.linspace(0, 4, 5)
y = function(x)

original_area = trapezoid(y, x=x)
exact_area = 4 ** 3 / 3

print("ORIGINAL RESULTS")
print("Estimated area:", round(original_area, 4))
print("Exact area:", round(exact_area, 4))
print("Absolute error:", round(abs(exact_area - original_area), 4))

# Modified input: upper limit changed from 4 to 5
x_new = np.linspace(0, 5, 6)
y_new = function(x_new)

new_area = trapezoid(y_new, x=x_new)
new_exact_area = 5 ** 3 / 3

print("\nMODIFIED RESULTS")
print("New estimated area:", round(new_area, 4))
print("New exact area:", round(new_exact_area, 4))
print("New absolute error:", round(abs(new_exact_area - new_area), 4))