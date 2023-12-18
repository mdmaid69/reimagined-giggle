  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import collections
def create_user_string():
        return collections.UserString()