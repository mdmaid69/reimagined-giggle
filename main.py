  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)