  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import collections
def create_user_string():
        return collections.UserString()