  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)