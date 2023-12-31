import heapq
def pop_push_heap(heap, item):
        return heapq.heapreplace(heap, item)
import shutil
def move_file(src, dst):
        shutil.move(src, dst)