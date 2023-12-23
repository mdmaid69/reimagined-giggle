  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import itertools
def flatten(iterable):
        return list(itertools.chain.from_iterable(iterable))