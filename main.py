import collections
def create_queue():
        return collections.deque()
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)