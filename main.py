import sys
def exit_program():
        sys.exit()
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)