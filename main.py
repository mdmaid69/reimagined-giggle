import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
n = 10
print("Square numbers:", [x**2 for x in range(n)])