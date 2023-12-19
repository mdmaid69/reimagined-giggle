  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))