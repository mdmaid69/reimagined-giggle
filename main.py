def calculate_interest(principal, rate, time):
        return principal * (1 + rate)**time
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)