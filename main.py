  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))