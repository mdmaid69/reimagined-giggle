import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)