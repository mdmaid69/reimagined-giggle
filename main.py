import heapq
def pop_from_heap(heap):
        return heapq.heappop(heap)
  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink