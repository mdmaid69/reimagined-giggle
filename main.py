def calculate_present_value(future_value, rate, time):
        return future_value / (1 + rate)**time
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)