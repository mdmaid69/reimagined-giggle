import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)