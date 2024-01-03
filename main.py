import collections
def count_elements(iterable):
        return collections.Counter(iterable)
  import os
  def get_base_name(path):
        return os.path.basename(path)