import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def get_current_directory():
        return os.getcwd()