  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))