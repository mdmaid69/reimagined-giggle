import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_file_flags(file_name):
        return os.stat(file_name).st_flags