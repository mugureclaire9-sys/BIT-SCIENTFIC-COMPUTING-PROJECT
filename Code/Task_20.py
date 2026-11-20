
import numpy as np

def estimate_pi(number_of_points):
    x = np.random.rand(number_of_points)
    y = np.random.rand(number_of_points)

    inside_circle = (x**2 + y**2) <= 1

    pi_estimate = 4 * np.sum(inside_circle) / number_of_points

    return pi_estimate

# Original input
np.random.seed(42)

original_points = 10000
original_pi = estimate_pi(original_points)

print("ORIGINAL RESULTS")
print("Number of points:", original_points)
print("Estimated value of pi:", round(original_pi, 4))

# Modified input
np.random.seed(42)

new_points = 100000
new_pi = estimate_pi(new_points)

print("\nMODIFIED RESULTS")
print("New number of points:", new_points)
print("Estimated value of pi:", round(new_pi, 4))
