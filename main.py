  import os
  def delete_file(file_name):
        os.remove(file_name)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)