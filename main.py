import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import shutil
def delete_directory(path):
        shutil.rmtree(path)