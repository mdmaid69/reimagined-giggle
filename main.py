n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)