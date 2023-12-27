  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare
import collections
def create_user_string():
        return collections.UserString()