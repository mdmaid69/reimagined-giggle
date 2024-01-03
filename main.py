  import os
  def get_base_name(path):
        return os.path.basename(path)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)