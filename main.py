import math
def calculate_factorial(n):
        return math.factorial(n)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b