  import os
  def split_path(path):
        return os.path.split(path)
import getpass
def get_username():
        return getpass.getuser()