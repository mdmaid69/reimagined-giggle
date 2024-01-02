import getpass
def get_username():
        return getpass.getuser()
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)