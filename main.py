  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))