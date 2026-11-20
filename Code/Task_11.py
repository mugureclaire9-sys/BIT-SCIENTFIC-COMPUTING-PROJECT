
def f(x):
    return x**2 - 4


def derivative(x):
    return 2 * x


def newton_raphson(x, tolerance=0.000001):
    iterations = 0

    while True:
        new_x = x - f(x) / derivative(x)
        iterations += 1

        if abs(new_x - x) < tolerance:
            return new_x, iterations

        x = new_x


def secant(x0, x1, tolerance=0.000001):
    iterations = 0

    while True:
        new_x = x1 - f(x1) * (x1 - x0) / (f(x1) - f(x0))
        iterations += 1

        if abs(new_x - x1) < tolerance:
            return new_x, iterations

        x0 = x1
        x1 = new_x


print("ORIGINAL RESULTS")

root1, count1 = newton_raphson(3)
root2, count2 = secant(3, 2.5)

print("Newton-Raphson root:", round(root1, 6))
print("Newton-Raphson iterations:", count1)
print("Secant root:", round(root2, 6))
print("Secant iterations:", count2)

# Modified equation: x^2 - 9 = 0
def new_f(x):
    return x**2 - 9


def new_derivative(x):
    return 2 * x


def modified_newton(x, tolerance=0.000001):
    iterations = 0

    while True:
        new_x = x - new_f(x) / new_derivative(x)
        iterations += 1

        if abs(new_x - x) < tolerance:
            return new_x, iterations

        x = new_x


print("\nMODIFIED RESULTS")

new_root, new_count = modified_newton(4)

print("Modified equation: x^2 - 9 = 0")
print("Newton-Raphson root:", round(new_root, 6))
print("Iterations:", new_count)
