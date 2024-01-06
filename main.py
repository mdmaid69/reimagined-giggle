  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))