import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
n = 10
print("Factorial numbers:", [1 if x == 0 else x * factorial(x - 1) for x in range(n)])