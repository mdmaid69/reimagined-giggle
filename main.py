  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))