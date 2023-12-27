  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))