  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import collections
def create_user_string():
        return collections.UserString()