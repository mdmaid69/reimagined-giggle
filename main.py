import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])