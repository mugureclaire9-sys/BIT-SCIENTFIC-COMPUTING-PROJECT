
def euler_method(step_size, end_x):
    x = 0
    y = 1

    while x < end_x:
        y = y + step_size * (x + y)
        x = round(x + step_size, 10)

    return y


print("ORIGINAL RESULTS")

h = 0.1
original_y = euler_method(h, 0.5)

print("Step size:", h)
print("Estimated y at x = 0.5:", round(original_y, 6))

print("\nMODIFIED RESULTS")

new_h = 0.05
modified_y = euler_method(new_h, 0.5)

print("New step size:", new_h)
print("Estimated y at x = 0.5:", round(modified_y, 6))
