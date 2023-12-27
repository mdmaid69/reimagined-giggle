  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))