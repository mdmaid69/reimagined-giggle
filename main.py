import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])