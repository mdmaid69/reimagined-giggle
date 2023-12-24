import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])