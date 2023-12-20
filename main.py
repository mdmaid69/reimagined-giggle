  import os
  def get_file_birthtime_ns(file_name):
        return os.stat(file_name).st_birthtime_ns
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))