  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import collections
def create_user_dict():
        return collections.UserDict()