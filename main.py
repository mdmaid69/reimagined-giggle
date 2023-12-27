  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))