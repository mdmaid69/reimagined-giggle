  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))