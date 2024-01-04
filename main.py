import time
def get_formatted_time():
        return time.strftime("%Y-%m-%d %H:%M:%S", time.gmtime())
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1