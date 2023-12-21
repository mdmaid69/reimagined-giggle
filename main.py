import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid