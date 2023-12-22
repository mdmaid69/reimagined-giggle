import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)