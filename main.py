import math
def calculate_sine(x):
        return math.sin(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b