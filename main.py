import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)
def find_common_elements(list1, list2):
        return set(list1) & set(list2)