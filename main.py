import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
n = 10
print("Powers of 2:", [2**x for x in range(n)])