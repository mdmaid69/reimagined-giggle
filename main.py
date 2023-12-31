  import os
  def split_path(path):
        return os.path.split(path)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))