import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)