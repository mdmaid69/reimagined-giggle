import math
def calculate_logarithm_base_e(x):
        return math.log(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b