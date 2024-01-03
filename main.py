  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))