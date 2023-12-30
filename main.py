  import os
  def split_path(path):
        return os.path.split(path)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)