import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_perpetuity(payment, rate):
        return payment / rate