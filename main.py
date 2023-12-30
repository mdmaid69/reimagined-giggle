import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])