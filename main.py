import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])