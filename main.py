import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def find_difference(list1, list2):
        return set(list1) - set(list2)