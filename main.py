  import os
  def get_file_ctime_ns(file_name):
        return os.stat(file_name).st_ctime_ns
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)