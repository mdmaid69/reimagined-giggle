import math
def calculate_permutations(n, k):
        return math.perm(n, k)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))