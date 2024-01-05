n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import math
def calculate_circle_circumference(radius):
        return 2 * math.pi * radius