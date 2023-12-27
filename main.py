  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)
import getpass
def get_password(prompt):
        return getpass.getpass(prompt)