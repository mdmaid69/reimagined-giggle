  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)