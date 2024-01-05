  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import collections
def create_priority_queue():
        return collections.deque()