import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def get_file_atime_ns(file_name):
        return os.stat(file_name).st_atime_ns