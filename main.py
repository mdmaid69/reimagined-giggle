  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import collections
def count_elements(iterable):
        return collections.Counter(iterable)