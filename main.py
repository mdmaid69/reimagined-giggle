  import os
  def get_file_atime(file_name):
        return os.stat(file_name).st_atime
import getpass
def get_username():
        return getpass.getuser()