import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_compound_interest(principal, rate, time):
        return principal * (1 + rate)**time - principal