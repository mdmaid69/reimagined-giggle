import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal