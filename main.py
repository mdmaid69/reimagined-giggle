import math
def calculate_absolute_value(x):
        return math.fabs(x)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])