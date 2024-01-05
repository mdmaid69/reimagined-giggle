import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_simple_interest(principal, rate, time):
        return principal * rate * time