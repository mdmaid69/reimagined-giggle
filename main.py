import getpass
def get_username():
        return getpass.getuser()
  import os
  def join_paths(path1, path2):
        return os.path.join(path1, path2)