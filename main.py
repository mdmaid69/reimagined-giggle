import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)