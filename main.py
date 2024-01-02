import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_roi(gain, cost):
        return (gain - cost) / cost