  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)
  import os
  def get_file_creation_time(file_name):
        return os.path.getctime(file_name)