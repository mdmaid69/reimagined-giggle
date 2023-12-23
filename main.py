import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)