  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import collections
def create_queue():
        return collections.deque()