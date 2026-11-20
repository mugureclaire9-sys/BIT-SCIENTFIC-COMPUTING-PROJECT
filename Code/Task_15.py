def f(x):
    return x ** 3

def central_difference(x, h):
    return (f(x + h) - f(x - h)) / (2 * h)

x = 2
true_derivative = 12

# Original step size
h = 0.1
original_result = central_difference(x, h)

print("ORIGINAL RESULTS")
print("Step size:", h)
print("Estimated derivative:", round(original_result, 5))
print("Absolute error:", round(abs(true_derivative - original_result), 5))

# Modified step size
h_new = 0.01
modified_result = central_difference(x, h_new)

print("\nMODIFIED RESULTS")
print("New step size:", h_new)
print("Estimated derivative:", round(modified_result, 5))
print("Absolute error:", round(abs(true_derivative - modified_result), 5))