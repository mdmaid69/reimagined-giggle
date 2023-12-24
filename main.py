  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))