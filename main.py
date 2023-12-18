import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)