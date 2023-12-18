import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)