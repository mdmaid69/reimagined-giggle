import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)