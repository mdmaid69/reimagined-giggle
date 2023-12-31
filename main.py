import math
def calculate_neper_number_to_power_x(x):
        return math.exp(x)
n = 10
print("Prime numbers:", [x for x in range(2, n) if all(x % i != 0 for i in range(2, int(x**0.5) + 1))])