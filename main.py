import math
def calculate_permutations(n, k):
        return math.perm(n, k)
n = 10
print("Even numbers:", [x for x in range(n) if x % 2 == 0])