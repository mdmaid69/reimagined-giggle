import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def calculate_perimeter_rectangle(l, w):
        return 2 * (l + w)