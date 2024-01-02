import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)