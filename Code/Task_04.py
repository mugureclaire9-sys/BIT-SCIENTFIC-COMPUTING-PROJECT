
import numpy as np

# Floating-point arithmetic
a = 0.1
b = 0.2
c = 0.3

print("FLOATING-POINT ERROR")
print("0.1 + 0.2 =", a + b)
print("Is the result equal to 0.3?", a + b == c)
print("Using np.isclose:", np.isclose(a + b, c))

# Absolute and relative error
true_value = np.sqrt(2)
approx_value = 1.414

absolute_error = abs(true_value - approx_value)
relative_error = absolute_error / abs(true_value)

print("\nERROR CALCULATION")
print("True value:", true_value)
print("Approximate value:", approx_value)
print("Absolute error:", absolute_error)
print("Relative error:", relative_error)

# Modified input
modified_value = 1.4142

modified_error = abs(true_value - modified_value)

print("\nMODIFIED RESULTS")
print("New approximate value:", modified_value)
print("New absolute error:", modified_error)
