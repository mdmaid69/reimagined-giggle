  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))