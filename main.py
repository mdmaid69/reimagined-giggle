import math
def calculate_sign(x):
        return math.copysign(1, x)
n = 10
print("Odd numbers:", [x for x in range(n) if x % 2 != 0])