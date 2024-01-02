  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))