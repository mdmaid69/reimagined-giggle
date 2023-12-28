  import os
  def get_file_nlink(file_name):
        return os.stat(file_name).st_nlink
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)