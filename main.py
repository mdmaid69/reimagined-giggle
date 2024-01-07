  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))