import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime