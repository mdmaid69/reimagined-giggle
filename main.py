import math
def calculate_combinations(n, k):
        return math.comb(n, k)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)