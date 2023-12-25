import math
def calculate_sign(x):
        return math.copysign(1, x)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])