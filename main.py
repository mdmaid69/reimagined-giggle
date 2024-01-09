import os
def create_directory(path):
        os.makedirs(path, exist_ok=True)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)