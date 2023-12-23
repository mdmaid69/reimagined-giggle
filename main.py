  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))