  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))