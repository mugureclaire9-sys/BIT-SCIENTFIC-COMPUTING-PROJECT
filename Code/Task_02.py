
import numpy as np

# 24 hourly temperature readings in Celsius
temperatures_c = np.array([
    18.5, 18.0, 17.8, 17.5, 17.9, 19.0,
    21.5, 23.8, 25.6, 27.1, 28.3, 29.0,
    29.4, 29.1, 28.5, 27.6, 26.2, 24.8,
    23.4, 22.1, 21.0, 20.2, 19.6, 19.0
])

# Original calculations
print("ORIGINAL RESULTS")
print("Mean:", round(np.mean(temperatures_c), 2), "C")
print("Minimum:", np.min(temperatures_c), "C")
print("Maximum:", np.max(temperatures_c), "C")

temperatures_f = 1.8 * temperatures_c + 32
print("First six Fahrenheit readings:", temperatures_f[:6])

# Modified input
modified_temperatures = temperatures_c.copy()
modified_temperatures[0] = 20.5

# Modified calculations
print("\nMODIFIED RESULTS")
print("Mean:", round(np.mean(modified_temperatures), 2), "C")
print("Minimum:", np.min(modified_temperatures), "C")
print("Maximum:", np.max(modified_temperatures), "C")

modified_f = 1.8 * modified_temperatures + 32
print("First six Fahrenheit readings:", modified_f[:6])
