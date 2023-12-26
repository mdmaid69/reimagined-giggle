import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)