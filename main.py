import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare