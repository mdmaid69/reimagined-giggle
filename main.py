  import os
  def get_file_name_without_extension(file_name):
        return os.path.splitext(file_name)[0]
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))