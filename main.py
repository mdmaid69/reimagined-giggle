import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid