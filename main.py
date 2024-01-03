import math
def calculate_arc_sine(x):
        return math.asin(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b