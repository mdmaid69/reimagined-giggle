list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Union:", set(list1) | set(list2))
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h