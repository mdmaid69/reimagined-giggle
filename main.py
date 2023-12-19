  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))