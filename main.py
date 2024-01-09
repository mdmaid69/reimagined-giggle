import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])