import math
def calculate_sign(x):
        return math.copysign(1, x)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)