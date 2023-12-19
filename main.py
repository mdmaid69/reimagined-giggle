def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)