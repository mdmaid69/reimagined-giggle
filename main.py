  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import collections
def create_chain_map(*maps):
        return collections.ChainMap(*maps)