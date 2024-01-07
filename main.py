  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))