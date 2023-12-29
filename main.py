  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import collections
def create_stack():
        return collections.deque()