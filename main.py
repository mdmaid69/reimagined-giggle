import math
def calculate_logarithm_base_10(x):
        return math.log10(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b