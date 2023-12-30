import math
def calculate_gamma_function(x):
        return math.gamma(x)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))