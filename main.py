  import os
  def get_file_gen(file_name):
        return os.stat(file_name).st_gen
import getpass
def get_username():
        return getpass.getuser()