import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])