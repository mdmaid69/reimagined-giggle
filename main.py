import shutil
def delete_directory(path):
        shutil.rmtree(path)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)