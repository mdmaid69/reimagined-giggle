def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)