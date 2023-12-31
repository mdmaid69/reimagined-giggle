  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))