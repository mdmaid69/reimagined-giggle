  import os
  def get_file_mtime_ns(file_name):
        return os.stat(file_name).st_mtime_ns
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)