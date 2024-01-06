import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))