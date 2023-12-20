import math
def calculate_circle_area(radius):
        return math.pi * radius**2
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))