import math
def calculate_sign(x):
        return math.copysign(1, x)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])