  import os
  def get_file_size(file_name):
        return os.stat(file_name).st_size
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)