import math
def calculate_combinations(n, k):
        return math.comb(n, k)
n = 10
print("Is prime:", all(n % i != 0 for i in range(2, int(n**0.5) + 1)))