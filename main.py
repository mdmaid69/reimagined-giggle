  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)