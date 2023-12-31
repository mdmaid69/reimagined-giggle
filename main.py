  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))