  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))