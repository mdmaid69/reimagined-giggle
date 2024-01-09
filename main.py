  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import collections
def count_elements(iterable):
        return collections.Counter(iterable)