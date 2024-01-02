import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])