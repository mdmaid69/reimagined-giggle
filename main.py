import math
def calculate_cartesian_to_polar_coordinates(x, y):
        return math.rect(x, y)
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1