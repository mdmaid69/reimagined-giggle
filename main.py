import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b