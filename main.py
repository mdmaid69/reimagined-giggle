import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
n = 5
result = 1
for i in range(1, n + 1):
        result *= i
print("Factorial:", result)