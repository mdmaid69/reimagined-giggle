import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)