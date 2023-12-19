  import os
  def get_file_lspare(file_name):
        return os.stat(file_name).st_lspare
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))