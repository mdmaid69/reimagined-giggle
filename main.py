  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))