  import os
  def delete_directory(dir_name):
        os.rmdir(dir_name)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)