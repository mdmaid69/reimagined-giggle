import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)