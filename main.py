import collections
def create_queue():
        return collections.deque()
  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino