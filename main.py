import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)