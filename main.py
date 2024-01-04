  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))