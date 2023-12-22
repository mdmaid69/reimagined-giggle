  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)