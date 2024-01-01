import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)