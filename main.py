import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)