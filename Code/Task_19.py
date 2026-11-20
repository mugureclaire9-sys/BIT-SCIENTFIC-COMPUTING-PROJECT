
from scipy.optimize import minimize

def function(x):
    return (x[0] - 3) ** 2 + 4

# Original optimization
original = minimize(function, [0])

print("ORIGINAL RESULTS")
print("Minimum x:", round(original.x[0], 4))
print("Minimum function value:", round(original.fun, 4))

# Modified function
def modified_function(x):
    return (x[0] - 5) ** 2 + 2

modified = minimize(modified_function, [0])

print("\nMODIFIED RESULTS")
print("Minimum x:", round(modified.x[0], 4))
print("Minimum function value:", round(modified.fun, 4))
