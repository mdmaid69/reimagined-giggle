import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)