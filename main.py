  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
import getpass
def get_username():
        return getpass.getuser()