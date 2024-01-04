  import os
  def get_file_block_size(file_name):
        return os.stat(file_name).st_blksize
import heapq
def push_pop_heap(heap, item):
        return heapq.heappushpop(heap, item)