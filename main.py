import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)