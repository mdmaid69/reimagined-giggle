import itertools
def get_permutations(iterable):
        return list(itertools.permutations(iterable))
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)