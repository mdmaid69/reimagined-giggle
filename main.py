import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
n = 10
print("Powers of 2:", [2**x for x in range(n)])