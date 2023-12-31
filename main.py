list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import heapq
def merge_sorted_iterables(*iterables):
        return heapq.merge(*iterables)