  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))