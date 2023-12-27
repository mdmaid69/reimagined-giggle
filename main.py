  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))