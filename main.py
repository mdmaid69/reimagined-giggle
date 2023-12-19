import collections
def create_stack():
        return collections.deque()
  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size