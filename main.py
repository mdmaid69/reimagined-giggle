import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)