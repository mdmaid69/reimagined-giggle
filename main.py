import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)