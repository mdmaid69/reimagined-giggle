def factorial(n):
        if n == 0:
        return 1
        else:
        return n * factorial(n-1)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))