import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)