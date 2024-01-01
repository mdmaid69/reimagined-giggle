n = 10
print("Cube numbers:", [x**3 for x in range(n)])
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))