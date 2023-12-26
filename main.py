import math
def calculate_permutations(n, k):
        return math.perm(n, k)
numbers = [1, 2, 3, 4, 5]
print("Even:", [n for n in numbers if n % 2 == 0])