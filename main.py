import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def remove_duplicates(lst):
        return list(set(lst))