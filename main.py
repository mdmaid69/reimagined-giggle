import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))