  import os
  def get_file_rdev(file_name):
        return os.stat(file_name).st_rdev
import getpass
def get_username():
        return getpass.getuser()