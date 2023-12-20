import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare