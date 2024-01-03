  import os
  def get_base_name(path):
        return os.path.basename(path)
import collections
def create_stack():
        return collections.deque()