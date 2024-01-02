import collections
def create_user_dict():
        return collections.UserDict()
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)