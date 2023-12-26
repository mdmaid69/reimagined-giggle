import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])