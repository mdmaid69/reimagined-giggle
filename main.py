import collections
def create_queue():
        return collections.deque()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)