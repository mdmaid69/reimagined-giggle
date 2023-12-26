import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b