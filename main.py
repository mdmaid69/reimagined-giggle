import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)