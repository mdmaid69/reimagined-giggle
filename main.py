import getpass
def get_username():
        return getpass.getuser()
  import os
  def get_directory_name(path):
        return os.path.dirname(path)