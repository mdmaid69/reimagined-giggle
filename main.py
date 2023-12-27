import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
numbers = [1, 2, 3, 4, 5]
print("Squared:", [n**2 for n in numbers])