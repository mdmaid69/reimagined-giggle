  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)