import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1
import math
def calculate_bessel_function_of_second_kind(n, x):
        return math.yn(n, x)