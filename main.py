import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen