n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))