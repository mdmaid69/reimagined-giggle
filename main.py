  import os
  def split_path(path):
        return os.path.split(path)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))