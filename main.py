import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)