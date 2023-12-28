import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)