import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)