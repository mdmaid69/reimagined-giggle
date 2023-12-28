  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))