  import os
  def get_file_device(file_name):
        return os.stat(file_name).st_dev
import collections
def create_user_list():
        return collections.UserList()