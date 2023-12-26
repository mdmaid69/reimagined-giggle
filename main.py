import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b