  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import collections
def count_elements(iterable):
        return collections.Counter(iterable)