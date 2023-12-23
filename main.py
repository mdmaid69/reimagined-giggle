import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)