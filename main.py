  import os
  def get_file_inode(file_name):
        return os.stat(file_name).st_ino
import collections
def create_counter():
        return collections.Counter()