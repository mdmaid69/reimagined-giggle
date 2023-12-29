n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b
import math
def calculate_complementary_error_function(x):
        return math.erfc(x)