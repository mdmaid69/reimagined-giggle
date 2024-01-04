  import os
  def get_file_ino(file_name):
        return os.stat(file_name).st_ino
import getpass
def get_username():
        return getpass.getuser()