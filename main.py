  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)
  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)