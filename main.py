  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)