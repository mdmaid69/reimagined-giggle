import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid