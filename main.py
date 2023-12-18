import collections
def create_queue():
        return collections.deque()
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)