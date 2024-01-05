import shutil
def move_file(src, dst):
        shutil.move(src, dst)
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)