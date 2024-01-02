  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))