import math
def calculate_cosine(x):
        return math.cos(x)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])