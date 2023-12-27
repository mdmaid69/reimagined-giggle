  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def check_if_directory_exists(dir_name):
        return os.path.isdir(dir_name)