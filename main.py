  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import collections
def count_elements(iterable):
        return collections.Counter(iterable)