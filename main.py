  import os
  def get_file_blksize(file_name):
        return os.stat(file_name).st_blksize
import getpass
def get_username():
        return getpass.getuser()