  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)