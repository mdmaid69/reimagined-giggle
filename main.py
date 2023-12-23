  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)