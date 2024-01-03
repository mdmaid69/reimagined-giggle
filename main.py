  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))