import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)