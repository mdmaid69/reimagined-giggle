import array
def get_array_as_dict(array):
        return {i: item for i, item in enumerate(array)}
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1