import math
def calculate_degrees_to_radians(degrees):
        return math.radians(degrees)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b