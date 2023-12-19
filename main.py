import math
def calculate_modulus(x, y):
        return math.fmod(x, y)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))