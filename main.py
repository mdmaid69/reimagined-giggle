import math
def calculate_bessel_function_of_first_kind(n, x):
        return math.jn(n, x)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)