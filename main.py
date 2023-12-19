import collections
def create_user_list():
        return collections.UserList()
  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns