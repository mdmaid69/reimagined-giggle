  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))