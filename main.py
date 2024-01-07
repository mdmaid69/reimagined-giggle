import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b