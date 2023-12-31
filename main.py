def fibonacci(n):
        a, b = 0, 1
        while a < n:
        print(a, end=" ")
        a, b = b, a+b
import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)