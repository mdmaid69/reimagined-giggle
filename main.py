import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))