import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time