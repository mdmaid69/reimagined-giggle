  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
import getpass
def get_username():
        return getpass.getuser()