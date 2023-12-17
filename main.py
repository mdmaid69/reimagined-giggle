  import os
  def get_directory_name(path):
        return os.path.dirname(path)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)