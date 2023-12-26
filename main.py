import collections
def create_queue():
        return collections.deque()
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]