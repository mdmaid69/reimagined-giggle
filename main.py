n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])
import math
def calculate_arc_cosine(x):
        return math.acos(x)