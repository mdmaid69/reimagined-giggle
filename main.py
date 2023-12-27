  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))