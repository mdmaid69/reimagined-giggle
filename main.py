import collections
def create_priority_queue():
        return collections.deque()
  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns