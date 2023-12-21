import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import shutil
def delete_directory(path):
        shutil.rmtree(path)