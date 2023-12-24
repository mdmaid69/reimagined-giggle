  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))