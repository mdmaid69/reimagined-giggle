import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def get_file_extension(file_name):
        return os.path.splitext(file_name)[1]