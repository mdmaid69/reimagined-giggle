import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)