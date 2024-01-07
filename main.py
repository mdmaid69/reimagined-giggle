import collections
def create_user_dict():
        return collections.UserDict()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)