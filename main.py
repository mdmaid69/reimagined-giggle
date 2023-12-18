import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))