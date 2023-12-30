import itertools
def get_cartesian_product(*iterables):
        return list(itertools.product(*iterables))
  import os
  def delete_file(file_name):
        os.remove(file_name)