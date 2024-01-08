import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)