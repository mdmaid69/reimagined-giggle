  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))