n = 10
print("Square numbers:", [x**2 for x in range(n)])
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))