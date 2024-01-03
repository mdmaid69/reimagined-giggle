import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])