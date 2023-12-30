  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import collections
def create_user_dict():
        return collections.UserDict()