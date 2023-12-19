import sys
def add_to_python_path(path):
        sys.path.append(path)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)