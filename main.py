  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)