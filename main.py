  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import collections
def create_stack():
        return collections.deque()