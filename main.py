import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)