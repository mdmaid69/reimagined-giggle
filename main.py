  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns
def find_min(lst):
        return min(lst)