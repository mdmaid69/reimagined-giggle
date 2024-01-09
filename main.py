import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)