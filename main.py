import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)