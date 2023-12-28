import getpass
def get_username():
        return getpass.getuser()
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)