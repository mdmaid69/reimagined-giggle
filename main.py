  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))