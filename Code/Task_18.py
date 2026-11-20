
from scipy.integrate import solve_ivp

def equation(t, y):
    return -2 * y

# Original input
initial_value = [1]
time_interval = (0, 2)

original = solve_ivp(
    equation,
    time_interval,
    initial_value,
    t_eval=[2]
)

print("ORIGINAL RESULTS")
print("Initial value:", initial_value[0])
print("Estimated value at t = 2:", round(original.y[0][-1], 6))

# Modified input
new_initial_value = [2]

modified = solve_ivp(
    equation,
    time_interval,
    new_initial_value,
    t_eval=[2]
)

print("\nMODIFIED RESULTS")
print("New initial value:", new_initial_value[0])
print("Estimated value at t = 2:", round(modified.y[0][-1], 6))
