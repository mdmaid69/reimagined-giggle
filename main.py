  import os
  def delete_file(file_name):
        os.remove(file_name)
import collections
def create_stack():
        return collections.deque()