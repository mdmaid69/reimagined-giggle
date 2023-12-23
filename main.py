import sys
def exit_program():
        sys.exit()
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)