import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]