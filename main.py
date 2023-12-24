import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)