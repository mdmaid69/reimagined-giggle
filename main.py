import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def delete_file(file_name):
        os.remove(file_name)