import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)