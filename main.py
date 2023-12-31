  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)