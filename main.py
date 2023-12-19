  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))