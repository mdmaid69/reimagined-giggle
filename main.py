import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_file_access_time(file_name):
        return os.path.getatime(file_name)