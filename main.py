  import os
  def get_current_working_directory():
        return os.getcwd()
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))