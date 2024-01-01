import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)