import math
def calculate_sign(x):
        return math.copysign(1, x)
n = 10
print("Powers of 2:", [2**x for x in range(n)])