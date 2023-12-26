import heapq
def get_smallest_elements(iterable, n):
        return heapq.nsmallest(n, iterable)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))