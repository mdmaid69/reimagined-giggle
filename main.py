import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def get_directory_name(path):
        return os.path.dirname(path)