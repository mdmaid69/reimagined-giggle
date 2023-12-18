import math
def calculate_sign(x):
        return math.copysign(1, x)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))