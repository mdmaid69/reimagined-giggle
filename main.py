  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)
import getpass
def get_username():
        return getpass.getuser()