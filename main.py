import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time