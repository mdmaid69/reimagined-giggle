import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import array
def check_if_array_does_not_contain_item(array, item):
        return item not in array