  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))