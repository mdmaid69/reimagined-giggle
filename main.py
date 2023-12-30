import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Common elements:", set(list1) & set(list2))