  import os
  def get_file_birthtime(file_name):
        return os.stat(file_name).st_birthtime
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)