  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))