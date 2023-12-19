  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def list_files_in_directory(dir_name):
        return os.listdir(dir_name)