  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import collections
def create_user_string():
        return collections.UserString()