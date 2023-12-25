list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import heapq
def get_largest_elements(iterable, n):
        return heapq.nlargest(n, iterable)