  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))