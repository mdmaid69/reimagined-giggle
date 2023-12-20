import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)