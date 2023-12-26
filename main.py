import math
def calculate_logarithm_base_2(x):
        return math.log2(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b