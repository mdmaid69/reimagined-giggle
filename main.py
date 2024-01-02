def fibonacci(n):
        return n if n <= 1 else fibonacci(n-1) + fibonacci(n-2)
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))