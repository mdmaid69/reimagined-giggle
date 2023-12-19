  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))