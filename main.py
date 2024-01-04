  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)