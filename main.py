def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)