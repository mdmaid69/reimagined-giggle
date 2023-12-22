import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
n = 10
print("Fibonacci:", [((1 + 5**0.5) / 2)**n / 5**0.5 for n in range(n)])