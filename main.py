  import os
  def get_file_gid(file_name):
        return os.stat(file_name).st_gid
import getpass
def get_username():
        return getpass.getuser()