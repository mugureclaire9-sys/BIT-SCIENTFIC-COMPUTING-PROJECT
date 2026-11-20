
import numpy as np

# Square coordinates
points = np.array([
    [0, 0],
    [1, 0],
    [1, 1],
    [0, 1]
])

# Transformation function
def transform(angle):
    radians = np.radians(angle)

    rotation = np.array([
        [np.cos(radians), -np.sin(radians)],
        [np.sin(radians), np.cos(radians)]
    ])

    scaling = np.array([
        [2.0, 0],
        [0, 1.5]
    ])

    transformation = rotation @ scaling
    new_points = points @ transformation.T

    return transformation, new_points

# Original rotation: 45 degrees
matrix, result = transform(45)

print("ORIGINAL RESULTS")
print("Transformation matrix:")
print(matrix)

print("\nNew coordinates:")
print(result)

print("\nDeterminant:", round(np.linalg.det(matrix), 2))

# Modified rotation: 90 degrees
new_matrix, new_result = transform(90)

print("\nMODIFIED RESULTS")
print("New coordinates:")
print(new_result)

print("\nDeterminant:", round(np.linalg.det(new_matrix), 2))
