  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))