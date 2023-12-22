  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
import getpass
def get_username():
        return getpass.getuser()