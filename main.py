import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import shutil
def copy_file(src, dst):
        shutil.copy(src, dst)