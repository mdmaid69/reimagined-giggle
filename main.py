import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)