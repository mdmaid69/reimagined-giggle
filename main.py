  import os
  def get_file_modification_time(file_name):
        return os.path.getmtime(file_name)
  import os
  def change_file_permissions(file_name, mode):
        os.chmod(file_name, mode)