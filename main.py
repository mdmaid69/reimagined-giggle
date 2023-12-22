  import os
  def delete_file(file_name):
        os.remove(file_name)
import getpass
def get_username():
        return getpass.getuser()