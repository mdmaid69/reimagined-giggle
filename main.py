  import os
  def get_file_dev(file_name):
        return os.stat(file_name).st_dev
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)