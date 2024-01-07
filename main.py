  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))