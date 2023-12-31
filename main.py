  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags
import getpass
def get_username():
        return getpass.getuser()