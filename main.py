  import os
  def get_current_working_directory():
        return os.getcwd()
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)