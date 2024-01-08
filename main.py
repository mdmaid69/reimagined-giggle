import getpass
def get_username():
        return getpass.getuser()
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)