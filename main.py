  import os
  def get_file_blocks_allocated(file_name):
        return os.stat(file_name).st_blocks
import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))