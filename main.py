  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import collections
def create_queue():
        return collections.deque()