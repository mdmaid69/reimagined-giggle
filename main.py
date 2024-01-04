  import os
  def get_file_uid(file_name):
        return os.stat(file_name).st_uid
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))