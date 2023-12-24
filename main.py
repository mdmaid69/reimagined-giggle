  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))