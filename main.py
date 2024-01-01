import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_amortization(principal, rate, time):
        return (principal * rate) / (1 - (1 + rate)**-time)