def calculate_average(lst):
        return sum(lst) / len(lst)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)