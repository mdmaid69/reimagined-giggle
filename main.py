  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))