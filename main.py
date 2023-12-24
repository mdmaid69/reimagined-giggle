import shutil
def delete_directory(path):
        shutil.rmtree(path)
import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)