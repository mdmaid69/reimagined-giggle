import collections
def count_elements(iterable):
        return collections.Counter(iterable)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))