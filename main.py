  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))