  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import collections
def count_elements(iterable):
        return collections.Counter(iterable)