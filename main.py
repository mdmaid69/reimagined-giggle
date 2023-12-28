import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])