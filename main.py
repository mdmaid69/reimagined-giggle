import math
def calculate_combinations(n, k):
        return math.comb(n, k)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))