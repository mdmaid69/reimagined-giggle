  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import collections
def create_stack():
        return collections.deque()