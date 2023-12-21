import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time