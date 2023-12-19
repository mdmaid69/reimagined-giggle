  import os
  def get_file_size_in_bytes(file_name):
        return os.stat(file_name).st_size
import collections
def count_elements(iterable):
        return collections.Counter(iterable)