import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def get_base_name(path):
        return os.path.basename(path)