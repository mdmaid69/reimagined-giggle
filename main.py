  import os
  def get_file_blocks(file_name):
        return os.stat(file_name).st_blocks
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)