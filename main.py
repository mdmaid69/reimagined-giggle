  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import itertools
def get_combinations(iterable, r):
        return list(itertools.combinations(iterable, r))