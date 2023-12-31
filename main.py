  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)