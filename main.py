list1 = [1, 2, 3]
list2 = [2, 3, 4]
print("Difference:", set(list1) - set(list2))
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)