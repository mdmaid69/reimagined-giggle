import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)