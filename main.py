import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def delete_file(file_name):
        os.remove(file_name)