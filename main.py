import getpass
def get_username():
        return getpass.getuser()
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)