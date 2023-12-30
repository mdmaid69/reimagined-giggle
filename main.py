import sys
def exit_program():
        sys.exit()
import heapq
def create_heap(iterable):
        h = list(iterable)
        heapq.heapify(h)
        return h