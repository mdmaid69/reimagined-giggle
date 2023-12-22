n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import math
def calculate_root(x, n):
        return math.pow(x, 1/n)