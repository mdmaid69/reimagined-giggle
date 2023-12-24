  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))