import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns