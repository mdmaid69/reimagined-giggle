  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)