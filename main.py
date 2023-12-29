import random
def shuffle_list(my_list):
        random.shuffle(my_list)
        return my_list
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1