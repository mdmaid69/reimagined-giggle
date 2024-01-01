def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)