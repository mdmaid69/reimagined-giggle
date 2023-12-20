import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time