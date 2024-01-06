def calculate_future_value(principal, rate, time):
        return principal * (1 + rate)**time
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)