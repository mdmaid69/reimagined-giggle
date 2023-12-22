import getpass
def get_username():
        return getpass.getuser()
  import os
  def get_base_name(path):
        return os.path.basename(path)