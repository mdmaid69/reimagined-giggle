  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
import getpass
def get_username():
        return getpass.getuser()