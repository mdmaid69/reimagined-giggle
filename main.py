import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
n = 10
a, b = 0, 1
while a < n:
        print(a, end=" ")
        a, b = b, a+b