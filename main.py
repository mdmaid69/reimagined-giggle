  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))