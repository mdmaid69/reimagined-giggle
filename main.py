import functools
print(functools.reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]))
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1