  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import collections
def create_stack():
        return collections.deque()