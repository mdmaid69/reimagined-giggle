  import os
  def create_directory(dir_name):
        os.makedirs(dir_name, exist_ok=True)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)