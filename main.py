import math
def calculate_root(x, n):
        return math.pow(x, 1/n)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))