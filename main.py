  import os
  def get_file_group(file_name):
        return os.stat(file_name).st_gid
import collections
def create_counter():
        return collections.Counter()