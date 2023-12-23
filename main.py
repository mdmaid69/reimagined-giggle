  import os
  def get_file_permissions(file_name):
        return os.stat(file_name).st_mode
import getpass
def get_username():
        return getpass.getuser()