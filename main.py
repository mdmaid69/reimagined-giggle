import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])