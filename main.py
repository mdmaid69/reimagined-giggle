  import os
  def get_file_mtime(file_name):
        return os.stat(file_name).st_mtime
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)