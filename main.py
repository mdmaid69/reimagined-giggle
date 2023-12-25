import math
def calculate_euclidean_norm(v):
        return math.hypot(*v)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)