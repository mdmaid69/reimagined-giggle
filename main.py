import math
def calculate_product_of_sequence(start, stop, step):
        return math.prod(range(start, stop, step))
def find_difference(list1, list2):
        return set(list1) - set(list2)