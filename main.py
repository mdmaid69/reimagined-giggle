import collections
def count_elements(iterable):
        return collections.Counter(iterable)
def find_union(list1, list2):
        return set(list1) | set(list2)