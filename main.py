  import os
  def get_file_owner(file_name):
        return os.stat(file_name).st_uid
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)