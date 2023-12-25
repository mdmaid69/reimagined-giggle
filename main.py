list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)