import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def get_directory_name(path):
        return os.path.dirname(path)