import heapq
def push_to_heap(heap, item):
        heapq.heappush(heap, item)
  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]