import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_file_qspare(file_name):
        return os.stat(file_name).st_qspare