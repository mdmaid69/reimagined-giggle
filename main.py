  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import collections
def count_elements(iterable):
        return collections.Counter(iterable)