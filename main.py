  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))