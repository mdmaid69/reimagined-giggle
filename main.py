import getpass
def get_password(prompt):
        return getpass.getpass(prompt)
  import os
  def rename_file(old_name, new_name):
        os.rename(old_name, new_name)