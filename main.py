import collections
def create_queue():
        return collections.deque()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)