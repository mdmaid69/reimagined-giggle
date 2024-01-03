import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b