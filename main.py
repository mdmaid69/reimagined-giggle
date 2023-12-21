  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
def find_union(list1, list2):
        return set(list1) | set(list2)