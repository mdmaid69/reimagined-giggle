import math
def calculate_pythagorean_theorem(a, b):
        return math.sqrt(a**2 + b**2)
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1