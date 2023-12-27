  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]
import getpass
def get_username():
        return getpass.getuser()