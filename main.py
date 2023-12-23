  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))