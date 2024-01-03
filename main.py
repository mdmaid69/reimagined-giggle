import sys
def add_to_python_path(path):
        sys.path.append(path)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)