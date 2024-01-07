  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))