  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))