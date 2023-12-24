  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import collections
def create_queue():
        return collections.deque()