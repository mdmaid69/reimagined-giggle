import math
def calculate_remainder(x, y):
        return math.remainder(x, y)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))