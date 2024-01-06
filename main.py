  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))