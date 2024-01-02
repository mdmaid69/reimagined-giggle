import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)