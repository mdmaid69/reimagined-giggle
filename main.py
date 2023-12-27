  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import collections
def count_elements(iterable):
        return collections.Counter(iterable)