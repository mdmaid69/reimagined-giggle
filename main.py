  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import collections
def create_user_list():
        return collections.UserList()