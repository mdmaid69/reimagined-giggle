  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))