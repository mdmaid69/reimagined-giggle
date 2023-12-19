import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)