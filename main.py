import math
def calculate_power(base, exponent):
        return math.pow(base, exponent)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))