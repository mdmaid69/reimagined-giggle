import math
def calculate_circle_area(radius):
        return math.pi * radius**2
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])