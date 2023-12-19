def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import bisect
def binary_search(sorted_list, item):
        i = bisect.bisect_left(sorted_list, item)
        if i != len(sorted_list) and sorted_list[i] == item:
        return i
        else:
        return -1