import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_base_name(path):
        return os.path.basename(path)