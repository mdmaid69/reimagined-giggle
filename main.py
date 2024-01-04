import math
def calculate_error_function(x):
        return math.erf(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b