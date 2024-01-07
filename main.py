import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def get_base_name(path):
        return os.path.basename(path)