import getpass
def get_username():
        return getpass.getuser()
  import os
  def get_parent_directory(dir_name):
        return os.path.dirname(dir_name)