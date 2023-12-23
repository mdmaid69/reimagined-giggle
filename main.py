import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)