import getpass
def get_username():
        return getpass.getuser()
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)