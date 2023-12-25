import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)