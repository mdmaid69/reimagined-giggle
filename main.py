  import os
  def get_directory_name(path):
        return os.path.dirname(path)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)