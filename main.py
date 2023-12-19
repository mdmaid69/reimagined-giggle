  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))