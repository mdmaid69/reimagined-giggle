def find_common_elements(list1, list2):
        return set(list1) & set(list2)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)