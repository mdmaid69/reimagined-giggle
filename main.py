n = 10
print("Powers of 2:", [2**x for x in range(n)])
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)