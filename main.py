import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)