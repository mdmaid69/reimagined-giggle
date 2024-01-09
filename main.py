import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]