  import os
  def get_absolute_path(file_name):
        return os.path.abspath(file_name)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)