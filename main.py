def calculate_mortgage(principal, rate, time):
        return (principal * rate * (1 + rate)**time) / ((1 + rate)**time - 1)
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)