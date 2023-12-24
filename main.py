  import os
  def split_path(path):
        return os.path.split(path)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)