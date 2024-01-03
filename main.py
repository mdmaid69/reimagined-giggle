import math
def calculate_hypotenuse(a, b):
        return math.sqrt(a**2 + b**2)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])