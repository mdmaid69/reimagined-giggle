import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)