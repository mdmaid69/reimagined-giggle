  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))