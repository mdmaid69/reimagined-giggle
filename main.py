import collections
def create_user_dict():
        return collections.UserDict()
  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink