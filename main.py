import collections
def create_user_dict():
        return collections.UserDict()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)