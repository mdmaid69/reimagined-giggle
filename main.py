  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))