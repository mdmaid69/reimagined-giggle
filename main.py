import shutil
def delete_directory(path):
        shutil.rmtree(path)
import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)