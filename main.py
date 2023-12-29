  import os
  def change_current_working_directory(dir_name):
        os.chdir(dir_name)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)