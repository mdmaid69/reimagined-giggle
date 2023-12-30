import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_file_size(file_name):
        return os.path.getsize(file_name)