  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))