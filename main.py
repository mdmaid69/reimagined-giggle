  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))