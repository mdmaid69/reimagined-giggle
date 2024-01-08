import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))
  import os
  def get_directory_name(path):
        return os.path.dirname(path)