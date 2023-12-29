  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)