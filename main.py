  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import collections
def create_priority_queue():
        return collections.deque()