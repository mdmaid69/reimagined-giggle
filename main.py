  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
import getpass
def get_username():
        return getpass.getuser()