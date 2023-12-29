import math
def calculate_circle_area(radius):
        return math.pi * radius**2
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b