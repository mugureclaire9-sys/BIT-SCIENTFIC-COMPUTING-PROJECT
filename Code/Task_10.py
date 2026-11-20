
def f(x):
    return x**3 - x - 2


def bisection(a, b, tolerance=0.000001):
    iterations = 0

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

        iterations += 1

    return (a + b) / 2, iterations


def fixed_point(x, tolerance=0.000001):
    iterations = 0

    while True:
        new_x = (x + 2) ** (1 / 3)
        iterations += 1

        if abs(new_x - x) < tolerance:
            return new_x, iterations

        x = new_x


print("ORIGINAL RESULTS")

root1, count1 = bisection(1, 2)
root2, count2 = fixed_point(1.5)

print("Bisection root:", round(root1, 6))
print("Bisection iterations:", count1)
print("Fixed-point root:", round(root2, 6))
print("Fixed-point iterations:", count2)

# Modified input: change the constant from 2 to 3
def modified_f(x):
    return x**3 - x - 3


def modified_bisection(a, b, tolerance=0.000001):
    iterations = 0

    while (b - a) / 2 > tolerance:
        c = (a + b) / 2

        if modified_f(a) * modified_f(c) < 0:
            b = c
        else:
            a = c

        iterations += 1

    return (a + b) / 2, iterations


print("\nMODIFIED RESULTS")

new_root, new_count = modified_bisection(1, 2)

print("New equation: x^3 - x - 3 = 0")
print("Bisection root:", round(new_root, 6))
print("Bisection iterations:", new_count)
