  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))