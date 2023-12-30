  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import collections
def create_user_dict():
        return collections.UserDict()