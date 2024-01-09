import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)