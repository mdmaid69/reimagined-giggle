  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)