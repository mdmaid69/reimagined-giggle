numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])
import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))