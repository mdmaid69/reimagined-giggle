  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def get_current_directory():
        return os.getcwd()