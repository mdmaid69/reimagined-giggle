  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import collections
def create_user_string():
        return collections.UserString()