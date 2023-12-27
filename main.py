  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import collections
def create_stack():
        return collections.deque()