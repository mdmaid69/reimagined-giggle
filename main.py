  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))