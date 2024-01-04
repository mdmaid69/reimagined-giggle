  import os
  def get_file_number_of_links(file_name):
        return os.stat(file_name).st_nlink
import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)