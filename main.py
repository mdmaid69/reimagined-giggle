  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))