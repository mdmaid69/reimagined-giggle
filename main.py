  import os
  def get_file_mode(file_name):
        return os.stat(file_name).st_mode
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)