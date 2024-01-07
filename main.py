import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def split_path(path):
        return os.path.split(path)