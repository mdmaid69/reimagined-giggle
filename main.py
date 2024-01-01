import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)