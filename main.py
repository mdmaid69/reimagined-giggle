import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
n = 10
print("Cube numbers:", [x**3 for x in range(n)])