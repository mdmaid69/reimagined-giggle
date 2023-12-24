import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)