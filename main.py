  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import collections
def create_stack():
        return collections.deque()