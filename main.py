n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])
import math
def calculate_cube_root(x):
        return math.pow(x, 1/3)