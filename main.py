list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)