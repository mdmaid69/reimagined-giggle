import getpass
def get_username():
        return getpass.getuser()
  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime