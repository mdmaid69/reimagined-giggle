  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def check_if_file_exists(file_name):
        return os.path.isfile(file_name)