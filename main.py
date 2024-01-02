import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)