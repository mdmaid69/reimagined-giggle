  import os
  def get_base_name(path):
        return os.path.basename(path)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))