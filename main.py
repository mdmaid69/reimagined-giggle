import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])