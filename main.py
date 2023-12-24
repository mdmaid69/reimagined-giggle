  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))