  import os
  def get_file_ctime(file_name):
        return os.stat(file_name).st_ctime
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)