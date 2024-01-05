  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))